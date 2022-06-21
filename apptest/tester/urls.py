from rest_framework import routers
from .api import TestViewSet


router = routers.DefaultRouter()
router.register('api/todo', TestViewSet, 'todo')


urlpatterns = router.urls

