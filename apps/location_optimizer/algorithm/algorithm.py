import numpy as np
import geojson

from backend.settings import GRID_STEP, EXPLANATIONS, FEATURES


# unite good zone with nearest
def unite_with_nearest(lat, lon, MULT=5):
    left_up = (lon - MULT * GRID_STEP, lat + MULT * GRID_STEP)
    left_down = (lon - MULT * GRID_STEP, lat - (MULT + 1) * GRID_STEP)
    right_up = (lon + (MULT + 1) * GRID_STEP, lat + MULT * GRID_STEP)
    right_down = (lon + (MULT + 1) * GRID_STEP, lat - (MULT + 1) * GRID_STEP)

    return geojson.Polygon([[left_up, right_up, right_down,
                             left_down, left_up]])


# format to geojson
def to_geojson(best_cells, scores, explanation):
    features = []
    for index, cell in enumerate(best_cells):
        polygon = unite_with_nearest(cell.latitude, cell.longitude)
        feature = geojson.Feature(geometry=polygon,
                                  properties={
                                              'id': index,
                                              'score': scores[index],
                                              'explanation': explanation[index]
                                             })
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

    normalize(X)

    for index in range(len(cells)):
        scores[index] = business_w @ X[index]

    best_variants_ind = np.argsort(-scores)[:3]
    best_cells = [cells.get(id=id_list[ind]) for ind in best_variants_ind]

    explanations = []

    for index in best_variants_ind:
        most_weight = np.argmax(business_w * X[index])
        explanations.append(EXPLANATIONS[most_weight])

    return to_geojson(best_cells, scores[best_variants_ind], explanations)
