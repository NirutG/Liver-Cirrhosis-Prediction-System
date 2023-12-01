from django.urls import path
from . import views

urlpatterns = [
    path('', views.stage_prediction, name='stage_prediction')
]