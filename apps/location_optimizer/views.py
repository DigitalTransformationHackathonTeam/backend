from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
import numpy as np

from business.models import Business, BusinessTag
from grid.models import Grid
from location_optimizer.algorithm.algorithm import find_best_district
from backend.settings import FEATURES


class FindBestDistrictView(generics.GenericAPIView):
    lookup_field = ('city', 'business_name')

    def get_cells(self):
        city = Grid.objects.get(city_name=self.kwargs[self.lookup_field[0]])
        return city.cells.all()

    def get_object(self):
        return get_object_or_404(Business,
                                 eng_name=self.kwargs[self.lookup_field[1]])

    def get(self, request, *args, **kwargs):
        result = find_best_district(self.get_object().to_numpy(),
                                    self.get_cells())
        response = Response(result, status=200)
        return response


class FindBestDistrictForCustomCategoriesView(generics.GenericAPIView):
    lookup_field = 'city'
    queryset = Business.objects.all()

    def get_cells(self):
        city = Grid.objects.get(city_name=self.kwargs[self.lookup_field])
        return city.cells.all()

    def get_weights(self):
        tags = self.request.query_params.getlist('tag', default=[])

        weights = np.zeros(len(FEATURES))

        for tag in tags:
            if not BusinessTag.objects.filter(eng_name=tag).exists():
                return None, False
            obj = BusinessTag.objects.get(eng_name=tag)
            obj_w = obj.to_numpy()
            weights += obj_w

        weights /= len(FEATURES)

        return weights, True

    def get(self, request, *args, **kwargs):
        weights, flag = self.get_weights()
        if not flag:
            return Response({'message': 'Теги некорректны'}, status=400)
        result = find_best_district(weights, self.get_cells())
        response = Response(result, status=200)
        return response
