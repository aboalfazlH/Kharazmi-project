from django.urls import path
from .views import HomePageView,GlobalSearchView


urlpatterns = [
    path('',HomePageView.as_view(),name="home-page"),
        path('search/', GlobalSearchView.as_view(), name='global-search'),
]