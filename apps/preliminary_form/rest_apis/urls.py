from django.urls import path
from apps.preliminary_form.rest_apis.views import api_detail_user



app_name = "preliminary_form"

urlpatterns = [

    path('<slug>/' , api_detail_user , name="detail"),
]