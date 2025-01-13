from . import views
from django.urls import path



urlpatterns = [
    path('smartwatch/calories/', views.health_data_form, name='health_data_form'),
]
