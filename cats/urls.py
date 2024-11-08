from rest_framework.routers import DefaultRouter
from .views import SpyCatViewSet

router = DefaultRouter()
router.register(r'spycats', SpyCatViewSet, basename='spycat')

urlpatterns = router.urls
