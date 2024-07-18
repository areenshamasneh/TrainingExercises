from django.contrib import admin
from django.urls import path, include, register_converter
from polls import converters
from debug_toolbar.toolbar import debug_toolbar_urls # type: ignore

register_converter(converters.YearConverter, 'yyyy')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('polls.urls')),
] + debug_toolbar_urls()
