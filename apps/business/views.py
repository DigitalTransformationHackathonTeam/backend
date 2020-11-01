from rest_framework.views import APIView
from rest_framework.response import Response

from business.models import Business


class BusinessesListView(APIView):

    def get(self, request, *args, **kwargs):
        goods = {'value': 'goods', 'label': 'Товары',
                 'children': []}
        services = {'value': 'services', 'label': 'Услуги',
                    'children': []}

        for obj in Business.objects.all():
            if obj.business_type == Business.GOODS:
                goods['children'].append({'value': obj.eng_name,
                                          'label': obj.business_name})
            else:
                services['children'].append({'value': obj.eng_name,
                                             'label': obj.business_name})

        return Response([goods, services], status=200)
