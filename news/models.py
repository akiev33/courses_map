from hashlib import blake2b
from django.db import models

from django.contrib.auth import get_user_model


User = get_user_model()


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    nonprofitorganization = models.ForeignKey('authentications.NonProfitOrganizationProfile', on_delete=models.CASCADE, null=True, blank=True)
    centre = models.ForeignKey('authentications.EducationCentreProfile', on_delete=models.CASCADE, null=True, blank=True)
    teacher = models.ForeignKey('authentications.TeacherProfile', on_delete=models.CASCADE, null=True, blank=True)
    employer = models.ForeignKey('authentications.EmployerProfile', on_delete=models.CASCADE, null=True, blank=True)
    photo1 = models.ImageField(null=True, blank=True)
    photo2 = models.ImageField(null=True, blank=True)
    photo3 = models.ImageField(null=True, blank=True)
    photo4 = models.ImageField(null=True, blank=True)
    photo5 = models.ImageField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    href = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    sale = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return f'Created: {self.user}, profile: {self.nonprofitorganization} {self.centre} {self.teacher} {self.employer}'


# class NewsNonProfitOrganization(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     nonprofitorganization = models.ForeignKey('authentications.NonProfitOrganizationProfile', on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     href = models.CharField(max_length=255, null=True, blank=True)
#     price = models.CharField(max_length=255, null=True, blank=True)
#     sale = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return f'Created: {self.user}, profile: {self.nonprofitorganization}'


# class NewsEducationCentre(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     centre = models.ForeignKey('authentications.EducationCentreProfile', on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     href = models.CharField(max_length=255, null=True, blank=True)
#     price = models.CharField(max_length=255, null=True, blank=True)
#     sale = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return f'Created: {self.user}, profile: {self.centre}'


# class NewsTeacherProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     teacher = models.ForeignKey('authentications.TeacherProfile', on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     href = models.CharField(max_length=255, null=True, blank=True)
#     price = models.CharField(max_length=255, null=True, blank=True)
#     sale = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return f'Created: {self.user}, profile: {self.teacher}'


# class NewsEmployerProfile(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
#     employer = models.ForeignKey('authentications.EmployerProfile', on_delete=models.CASCADE, null=True, blank=True)
#     title = models.CharField(max_length=255)
#     description = models.TextField()
#     href = models.CharField(max_length=255, null=True, blank=True)
#     price = models.CharField(max_length=255, null=True, blank=True)
#     sale = models.CharField(max_length=255, null=True, blank=True)

#     def __str__(self):
#         return f'Created: {self.user}, profile: {self.employer}'

