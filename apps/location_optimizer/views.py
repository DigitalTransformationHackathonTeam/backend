from rest_framework import generics
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from business.models import Business
from grid.models import Grid
from location_optimizer.algorithm.algorithm import find_best_district


plug = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {
        "id": 1,
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              37.643280029296875,
              55.781400022214804
            ],
            [
              37.63315200805664,
              55.78062774182662
            ],
            [
              37.62800216674805,
              55.77357997618973
            ],
            [
              37.64276504516601,
              55.77039358162004
            ],
            [
              37.648773193359375,
              55.7765730186677
            ],
            [
              37.643280029296875,
              55.781400022214804
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": 2,
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              37.644996643066406,
              55.74895106540675
            ],
            [
              37.65512466430664,
              55.741511042163125
            ],
            [
              37.67040252685547,
              55.746728869390815
            ],
            [
              37.657527923583984,
              55.75503730199233
            ],
            [
              37.644996643066406,
              55.74895106540675
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": 3,
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              37.56568908691406,
              55.784875094551765
            ],
            [
              37.5847434997558,
              55.7761868325538
            ],
            [
              37.596588134765625,
              55.78381329977642
            ],
            [
              37.58749008178711,
              55.792499861438934
            ],
            [
              37.57427215576172,
              55.79172780105931
            ],
            [
              37.56568908691406,
              55.784875094551765
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {
        "id": 4,
      },
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              37.55744934082031,
              55.73049333764306
            ],
            [
              37.55470275878906,
              55.72179295289017
            ],
            [
              37.569122314453125,
              55.71840894635902
            ],
            [
              37.58354187011719,
              55.72817342459669
            ],
            [
              37.57427215576172,
              55.733682992998176
            ],
            [
              37.55744934082031,
              55.73049333764306
            ]
          ]
        ]
      }
    }
  ]
}


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
        # print('result:', str(ind), flush=True)
        response = Response(result, status=200)
        return response
