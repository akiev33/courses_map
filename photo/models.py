from django.db import models


class EducationCentrePhoto(models.Model):
    centre = models.ForeignKey('authentications.EducationCentreProfile', on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class TeacherProfilePhoto(models.Model):
    centre = models.ForeignKey('authentications.TeacherProfile', on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class NonProfitOrganizationProfilePhoto(models.Model):
    centre = models.ForeignKey('authentications.NonProfitOrganizationProfile', on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'


class EmployerProfilePhoto(models.Model):
    centre = models.ForeignKey('authentications.EmployerProfile', on_delete=models.CASCADE)
    image = models.ImageField()
    name = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.name}'