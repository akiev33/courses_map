from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import (NewsNonProfitOrganizationAPIView, NewsEducationCentreAPIView, NewsEmployerProfileAPIView, NewsTeacherProfileAPIView)
from .views import (NewsAPIView)


router = SimpleRouter()
router.register("", NewsAPIView)


urlpatterns = [

]
urlpatterns += router.urls