from django.urls import path
from . import views

# map the views to urls
urlpatterns = [
    path('', views.index, name='home-page'),
]