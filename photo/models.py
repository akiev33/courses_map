from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class EducationCentrePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    centre = models.ForeignKey('authentications.EducationCentreProfile', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class TeacherProfilePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey('authentications.TeacherProfile', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class NonProfitOrganizationProfilePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nonprofitorganization = models.ForeignKey('authentications.NonProfitOrganizationProfile', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class EmployerProfilePhoto(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    employer = models.ForeignKey('authentications.EmployerProfile', on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'