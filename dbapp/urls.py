from django.urls import path 
from . import views

urlpatterns = [
    path('db/', views.PersonDetailView.as_view(), name='home'),
    path("city/", views.PersonsInCityView.as_view(), name='city'),
]
