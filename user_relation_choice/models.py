from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRelationChoiceEducationCentreProfile(models.Model):
    
    RATE_CHOICES = (
        (1, 'Плохо'),
        (2, 'Мне не очень понравилось'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отличная статья')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey('authentications.EducationCentreProfile', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'{self.user}, Comments from: {self.profile}'


class UserRelationChoiceTeacherProfile(models.Model):
    
    RATE_CHOICES = (
        (1, 'Плохо'),
        (2, 'Мне не очень понравилось'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отличная статья')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey('authentications.TeacherProfile', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'{self.user}, Comments from: {self.profile}'


class UserRelationChoiceCourses(models.Model):
    
    RATE_CHOICES = (
        (1, 'Плохо'),
        (2, 'Мне не очень понравилось'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отличная статья')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey('authentications.TeacherProfile', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'{self.user}, Comments from: {self.profile}'


class UserRelationChoiceInternShip(models.Model):
    
    RATE_CHOICES = (
        (1, 'Плохо'),
        (2, 'Мне не очень понравилось'),
        (3, 'Нормально'),
        (4, 'Хорошо'),
        (5, 'Отличная статья')
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey('authentications.TeacherProfile', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'{self.user}, Comments from: {self.profile}'




