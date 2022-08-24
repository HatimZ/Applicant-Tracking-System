
from django.contrib import admin
from django.urls import path , include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('apply/'  , include('apps.preliminary_form.urls')),
    path('api/details/' , include('apps.preliminary_form.rest_apis.urls' ) )
]
