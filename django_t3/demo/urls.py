from django.views.generic.base import View
from django.db.models import fields
from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from .serializers import DPostsViewSet, DOptionsViewSet, DUsermetaViewSet, DUsersViewSet
from .views import ExampleView


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', DPostsViewSet)
router.register(r'options', DOptionsViewSet)
# router.register(r'usermeta', DUsermetaViewSet)
# router.register(r'users', DUsersViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('example', ExampleView.as_view()),
    path('', include(router.urls)),
]
