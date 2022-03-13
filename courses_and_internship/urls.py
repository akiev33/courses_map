from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (CoursesAPIView, InternShipAPIView)

router = SimpleRouter()
router.register("courses", CoursesAPIView)
router.register("intership", InternShipAPIView)


urlpatterns = [

]
urlpatterns += router.urls