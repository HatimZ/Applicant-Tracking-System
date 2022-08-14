from django.urls import path , include
from . import views


urlpatterns = [
    path('get_form/' , views.get_form),
    path('get_ending/' , views.get_ending)
]

