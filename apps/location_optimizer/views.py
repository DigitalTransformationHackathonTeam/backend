from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from business.models import Business
from grid.models import Grid
from location_optimizer.algorithm.algorithm import find_best_district


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

    def get_object(self):
        return get_object_or_404(Business,
                                 eng_name=self.kwargs[self.lookup_field])

    def get(self, request, *args, **kwargs):
        # result = find_best_district(self.get_object().to_numpy(),
                                    # self.get_cells())
        print(request.query_params, flush=True)
        response = Response(status=200)
        return response
