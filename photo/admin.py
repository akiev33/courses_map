from django.contrib import admin
from .models import (EducationCentrePhoto, TeacherProfilePhoto, EmployerProfilePhoto, NonProfitOrganizationProfilePhoto)


admin.site.register(EducationCentrePhoto)
admin.site.register(TeacherProfilePhoto)
admin.site.register(EmployerProfilePhoto)
admin.site.register(NonProfitOrganizationProfilePhoto)

