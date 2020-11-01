import numpy as np
import geojson
from scipy.special import expit
from sklearn.preprocessing import MinMaxScaler

from backend.settings import GRID_STEP, EXPLANATIONS, FEATURES


def is_intersection(coords_1, coords_2):
    lat_min = min(v[1] for v in coords_2)
    lat_max = max(v[1] for v in coords_2)
    lon_min = min(v[0] for v in coords_2)
    lon_max = max(v[0] for v in coords_2)

    for corner in coords_1:
        lat = corner[1]
        lon = corner[0]
        if lat_min <= lat <= lat_max and lon_min <= lon <= lon_max:
            return True

    return False


# unite good zone with nearest
def unite_with_nearest(lat, lon, MULT=3.5):
    left_up = (lon - MULT * GRID_STEP, lat + MULT * GRID_STEP)
    left_down = (lon - MULT * GRID_STEP, lat - (MULT + 1) * GRID_STEP)
    right_up = (lon + (MULT + 1) * GRID_STEP, lat + MULT * GRID_STEP)
    right_down = (lon + (MULT + 1) * GRID_STEP, lat - (MULT + 1) * GRID_STEP)

    return [left_up, right_up, right_down, left_down, left_up]


# format to geojson
def to_geojson(best_cells, scores, explanation):
    polygons = []
    for index, cell in enumerate(best_cells):
        polygon = unite_with_nearest(cell.latitude, cell.longitude)
        polygons.append(polygon)

    count = [True] * len(polygons)

    for i in range(len(polygons) - 1):
        for j in range(len(polygons) - 1, i, -1):
            if count[i] and is_intersection(polygons[i], polygons[j]):
                count[j] = False

    features = []
    index = 0
    for ind, polygon in enumerate(polygons):
        if count[ind]:
            polygon = geojson.Polygon([polygon])
            feature = geojson.Feature(geometry=polygon,
                                      properties={
                                        'id': index,
                                        'score': scores[ind],
                                        'explanation': explanation[ind]
                                      })
            index += 1
            features.append(feature)

    return geojson.FeatureCollection(features)


# normalize data
def normalize(X):
    min_val = X.min(axis=0)
    max_val = X.max(axis=0)
    X = (X - min_val) / (max_val - min_val)
    return X


def find_best_district(business_w, cells):
    id_list = [cell.id for cell in cells]
    scores = np.zeros(len(cells))

    X = np.zeros((len(cells), len(FEATURES)))

    for index, cell in enumerate(cells):
        X[index] = cell.to_numpy()

    scaler = MinMaxScaler()
    X = scaler.fit_transform(X)

    for index in range(len(cells)):
        scores[index] = business_w @ X[index]

    best_variants_ind = np.argsort(-scores)[:8]
    best_scores = scores[best_variants_ind]

    if np.std(best_scores) != 0:
        best_scores = (best_scores - np.mean(best_scores)) /\
                        np.std(best_scores)
    else:
        best_scores = best_scores - np.mean(best_scores)

    best_scores = expit(best_scores + 0.75) * 100

    best_cells = [cells.get(id=id_list[ind]) for ind in best_variants_ind]

    explanations = []

    for index in best_variants_ind:
        most_weight = np.argmax(business_w * X[index])
        explanations.append(EXPLANATIONS[most_weight])

    return to_geojson(best_cells, best_scores, explanations)
