import numpy as np
import geojson

from backend.settings import GRID_STEP


def to_geojson(best_cells):
    features = []
    for index, cell in enumerate(best_cells):
        left_up = (cell.longitude, cell.latitude)
        left_down = (cell.longitude, cell.latitude - GRID_STEP)
        right_up = (cell.longitude + GRID_STEP, cell.latitude)
        right_down = (cell.longitude + GRID_STEP, cell.latitude - GRID_STEP)
        polygon = geojson.Polygon([[left_up, right_up, right_down,
                                    left_down, left_up]])
        feature = geojson.Feature(geometry=polygon, properties={'id': index})
        features.append(feature)

    return geojson.FeatureCollection(features)


def normalize(x):
    if np.all(x == 0):
        return x
    return (x - np.mean(x)) / np.std(x)


def find_best_district(business_w, cells):
    id_list = [cell.id for cell in cells]
    scores = np.zeros(len(cells))

    X = np.zeros((len(cells), 2))

    for index, cell in enumerate(cells):
        X[index] = cell.to_numpy()

    X = normalize(X)

    for index in range(len(cells)):
        scores[index] = business_w @ X[index]

    best_variants_ind = np.argsort(-scores)[:5]
    best_cells = [cells.get(id=id_list[ind]) for ind in best_variants_ind]
    return to_geojson(best_cells)
