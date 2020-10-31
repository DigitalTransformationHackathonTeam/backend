from django.urls import path

from location_optimizer.views import FindBestDistrictView, \
                                     FindBestDistrictForCustomCategoriesView

urlpatterns = [
    path('find_best_district/<slug:city>/<slug:business_name>',
         FindBestDistrictView.as_view()),
    path('find_best_for_category/<slug:city>',
         FindBestDistrictForCustomCategoriesView.as_view()),
]
