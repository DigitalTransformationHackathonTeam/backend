from rest_framework import generics
from rest_framework.response import Response


plug = {
  "type": "FeatureCollection",
  "features": [
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              37.52975821495056,
              55.89540251375886
            ],
            [
              37.528685331344604,
              55.89412716085479
            ],
            [
              37.53051996231079,
              55.893020216805354
            ],
            [
              37.53335237503052,
              55.8928517660294
            ],
            [
              37.532655000686646,
              55.89506563216029
            ],
            [
              37.530702352523804,
              55.895829627294695
            ],
            [
              37.52975821495056,
              55.89540251375886
            ]
          ]
        ]
      }
    },
    {
      "type": "Feature",
      "properties": {},
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              37.734646797180176,
              55.69606714863728
            ],
            [
              37.72275924682617,
              55.689608860343014
            ],
            [
              37.74619102478027,
              55.6854720927719
            ],
            [
              37.75172710418701,
              55.69142309402056
            ],
            [
              37.7461051940918,
              55.70010606004817
            ],
            [
              37.74069786071777,
              55.69604296228203
            ],
            [
              37.734432220458984,
              55.69597040312637
            ],
            [
              37.734689712524414,
              55.69608528839396
            ],
            [
              37.734646797180176,
              55.69606714863728
            ]
          ]
        ]
      }
    }
  ]
}


class FindBestDistrictView(generics.GenericAPIView):
    def get(self, request, *args, **kwargs):
        response = Response(plug, status=200)
        response['Access-Control-Allow-Origin'] = '*'
        return response
