from django.contrib import admin

from .models import User, UserProfile, EducationCentreProfile, TeacherProfile, NonProfitOrganizationProfile,\
                    EmployerProfile


admin.site.register(User)
admin.site.register(UserProfile)
admin.site.register(EducationCentreProfile)
admin.site.register(TeacherProfile)
admin.site.register(NonProfitOrganizationProfile)
admin.site.register(EmployerProfile)
