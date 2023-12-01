from django.urls import path
from . import views

urlpatterns = [
    path('', views.survival_prediction, name='survival_prediction')
]