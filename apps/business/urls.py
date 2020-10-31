from django.urls import path

from business.views import BusinessesListView

urlpatterns = [
    path("businesses_list", BusinessesListView.as_view())
]
