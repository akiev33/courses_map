from django.urls import path
from rest_framework.routers import SimpleRouter
# from .views import (NewsNonProfitOrganizationAPIView, NewsEducationCentreAPIView, NewsEmployerProfileAPIView, NewsTeacherProfileAPIView)
from .views import (NewsAPIView)


router = SimpleRouter()
# router.register("nonprofitorganization_news", NewsNonProfitOrganizationAPIView)
# router.register("centre_news", NewsEducationCentreAPIView)
# router.register("employer_news", NewsEmployerProfileAPIView)
# router.register("teacher_news", NewsTeacherProfileAPIView)
router.register("", NewsAPIView)


urlpatterns = [

]
urlpatterns += router.urls