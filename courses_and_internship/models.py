from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth import get_user_model


User = get_user_model()


class Courses(models.Model):

    FORMATS_CHOICES = (
        (1, 'Онлайн'),
        (2, 'Оффлайн')
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    whats_app = PhoneNumberField()
    courses_name = models.CharField(max_length=250)
    description = models.TextField()
    phone_number = PhoneNumberField()
    email = models.EmailField(_('email address'), max_length=255, unique=True)
    instagram = models.CharField(max_length=250)
    video = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    number_of_free_places = models.PositiveIntegerField()
    rate = models.PositiveIntegerField()
    category = models.ManyToManyField('categories.Category')
    cost_per_month = models.PositiveIntegerField()
    time_table = models.CharField(max_length=255)
    lesson_duration = models.CharField(max_length=255)
    programm = models.TextField()
    sale = models.CharField(max_length=255, null=True, blank=True)
    formats = models.PositiveSmallIntegerField(choices=FORMATS_CHOICES)
    courses_duration = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.user}, Courses name: {self.courses_name}'


class InternShip(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    description = models.TextField()
    salary = models.CharField(max_length=255)
    time_table = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    rate = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.user}, Position: {self.position}, Salary: {self.salary}'