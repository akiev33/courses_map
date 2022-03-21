from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


class UserRelationChoiceEducationCentreProfile(models.Model):
    
    RATE_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey('authentications.EducationCentreProfile', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'{self.user}, Comments from: {self.profile}'


class UserRelationChoiceTeacherProfile(models.Model):
    
    RATE_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    profile = models.ForeignKey('authentications.TeacherProfile', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'{self.user}, Comments from: {self.profile}'


class UserRelationChoiceCourses(models.Model):
    
    RATE_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ForeignKey('courses_and_internship.Courses', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'{self.user}, Comments from: {self.course}'


class UserRelationChoiceInternShip(models.Model):
    
    RATE_CHOICES = (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5)
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    internship = models.ForeignKey('courses_and_internship.InternShip', on_delete=models.CASCADE)
    rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
    comments = models.TextField()

    def __str__(self):
        return f'{self.user}, Comments from: {self.internship}'




