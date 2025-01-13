from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.new_url,name="new_url"),
    path('home/',views.home,name="Home"),
    path('projects/',views.header,name="header"),
    path('about/',views.about,name="About"),
    path('contact/',views.contact,name="contact"),
    path('project/',include('MyApp.smartwatch.urls'))
]