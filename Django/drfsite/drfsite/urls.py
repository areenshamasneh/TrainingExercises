from django.contrib import admin
from django.urls import path, include
from rest_framework import routers # type: ignore
from rest_framework_nested import routers as nested_routers # type: ignore
from polls import views
from debug_toolbar.toolbar import debug_toolbar_urls  # type: ignore

router = routers.DefaultRouter()
router.register(r'polls', views.PollViewSet)

polls_router = nested_routers.NestedSimpleRouter(router, r'polls', lookup='poll')
polls_router.register(r'choices', views.ChoiceViewSet, basename='poll-choices')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(polls_router.urls)),
    path('admin/', admin.site.urls),
]  + debug_toolbar_urls()
