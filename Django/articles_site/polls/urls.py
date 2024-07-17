from django.urls import path, register_converter
from . import views
from .converters import YearConverter

register_converter(YearConverter, 'yyyy')

urlpatterns = [
    path('', views.home, name='home'),
    path('articles/', views.all_articles, name='all_articles'),
    path('articles/<yyyy:year>/', views.articles_by_year, name='articles_by_year'),
    path('articles/<yyyy:year>/<int:month>/',
         views.articles_by_month, name='articles_by_month'),
    path('articles/<yyyy:year>/<int:month>/<slug:slug>/',
         views.article_detail, name='article_detail'),
]
