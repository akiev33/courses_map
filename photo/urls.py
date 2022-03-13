from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import (EducationCentrePhotoAPIView, TeacherProfilePhotoAPIView, EmployerProfilePhotoAPIView, NonProfitOrganizationProfilePhotoAPIView)

router = SimpleRouter()
router.register("education_photo", EducationCentrePhotoAPIView)
router.register("teacher_photo", TeacherProfilePhotoAPIView)
router.register("employer_photo", EmployerProfilePhotoAPIView)
router.register("nonprofitorganization_photo", NonProfitOrganizationProfilePhotoAPIView)


urlpatterns = [

]
urlpatterns += router.urls