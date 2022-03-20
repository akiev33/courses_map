
from rest_framework.routers import SimpleRouter
from .views import FavoriteAPIView

router = SimpleRouter()
router.register("", FavoriteAPIView)

urlpatterns = []
urlpatterns += router.urls