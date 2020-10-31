from django.urls import path

from location_optimizer.views import FindBestDistrictView

urlpatterns = [
    path('find_best_district/<slug:city>/<slug:business_name>',
         FindBestDistrictView.as_view()),
]
