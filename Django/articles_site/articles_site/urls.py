from django.contrib import admin
from django.urls import path, include, register_converter
from polls import converters

register_converter(converters.YearConverter, 'yyyy')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
]
