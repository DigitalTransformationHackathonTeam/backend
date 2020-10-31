import numpy as np
import geojson

from backend.settings import GRID_STEP, EXPLANATIONS


def unite_with_nearest(lat, lon, MULT=5):
    left_up = (lon - MULT * GRID_STEP, lat + MULT * GRID_STEP)
    left_down = (lon - MULT * GRID_STEP, lat - (MULT + 1) * GRID_STEP)
    right_up = (lon + (MULT + 1) * GRID_STEP, lat + MULT * GRID_STEP)
    right_down = (lon + (MULT + 1) * GRID_STEP, lat - (MULT + 1) * GRID_STEP)

    return geojson.Polygon([[left_up, right_up, right_down,
                             left_down, left_up]])


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


def normalize(x):
    if np.all(x == 0):
        return x
    for col_ind in range(x.shape[1]):
        column = x[:, col_ind]
        min_val = np.min(column)
        x[:, col_ind] = (column - min_val) / (np.max(column) - min_val)

    return x


def find_best_district(business_w, cells):
    id_list = [cell.id for cell in cells]
    scores = np.zeros(len(cells))

    X = np.zeros((len(cells), 2))

    for index, cell in enumerate(cells):
        X[index] = cell.to_numpy()

    normalize(X)
    for index in range(len(cells)):
        scores[index] = business_w @ X[index]

    best_variants_ind = np.argsort(-scores)[:5]
    best_cells = [cells.get(id=id_list[ind]) for ind in best_variants_ind]

    explanations = []

    for index in best_variants_ind:
        most_weight = np.argmax(business_w * X[index])
        explanations.append(EXPLANATIONS[most_weight])

    return to_geojson(best_cells, scores[best_variants_ind], explanations)
