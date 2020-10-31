import csv
from typing import List

import numpy as np


class Business:
    def __init__(self, type_name: str):
        self.businessType: BusinessType = BusinessType(type_name)


class BusinessType:
    def __init__(self, type_name: str):
        self.type = type_name
        self.weight = np.array([])

        # Load weights vector for this business type
        self.load_weights()

    def load_weights(self):
        with open('category_factor_weights.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            factors = next(csv_reader)[1:]
            for row in csv_reader:
                if row[0] == self.type:
                    self.weight = np.array(list(map(int, row[1:])))
