from django.db.models import fields
from django.urls import path, include
from rest_framework import routers

from .serializers import DPostsViewSet, DOptionsViewSet, DUsermetaViewSet, DUsersViewSet


# Routers provide a way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'posts', DPostsViewSet)
router.register(r'options', DOptionsViewSet)
router.register(r'usermeta', DUsermetaViewSet)
router.register(r'users', DUsersViewSet)


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]
