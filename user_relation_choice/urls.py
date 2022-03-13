from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (UserRelationChoiceTeacherProfileAPIView, UserRelationChoiceEducationCentreProfileAPIView, UserRelationChoiceCoursesAPIView, UserRelationChoiceInternShipAPIView)

router = SimpleRouter()
router.register("teacher", UserRelationChoiceTeacherProfileAPIView)
router.register("centre", UserRelationChoiceEducationCentreProfileAPIView)
router.register("courses", UserRelationChoiceCoursesAPIView)
router.register("internship", UserRelationChoiceInternShipAPIView)


urlpatterns = [

]
urlpatterns += router.urls