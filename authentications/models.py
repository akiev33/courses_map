import uuid
from django.contrib.auth.base_user import BaseUserManager, AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from main.settings import AUTH_USER_MODEL
from phonenumber_field.modelfields import PhoneNumberField

from categories.models import Category


class UserManager(BaseUserManager):

    def create_user(self, email, password=None, **kwargs):
        email = self.normalize_email(email)
        user = self.model(email=email, **kwargs)
        user.set_password(password)
        user.create_activation_code()
        user.save(using=self._db)
        return user

    def create_superuser(self, **kwargs):
        user = self.create_user(**kwargs)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class AbstractEmailUser(AbstractBaseUser, PermissionsMixin):
    
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    is_staff = models.BooleanField(_('staff status'), default=True,
                                   help_text=_('Designates whether the user can log into this admin '
                                               'site.'))
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as '
                                                'active. Unselect this instead of deleting accounts.'))
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        abstract = True
        ordering = ['email']

    def get_full_name(self):
        return self.email

    def get_short_name(self):
        return self.email


class User(AbstractEmailUser):
    USER_TYPE_CHOICES = (
        ('user', 'User'),
        ('education_centre', 'EducationCentre'),
        ('teacher', 'Teacher'),
        ('non_profit_organization', 'Non-profit Organization'),
        ('employer', 'Employer')
    )

    user_type = models.CharField(choices=USER_TYPE_CHOICES, max_length=255, blank=True)

    image = models.ImageField(null=True, blank=True)
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)
    father_name = models.CharField('father_name', max_length=100)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    activation_code = models.CharField(max_length=36, blank=True)

    def get_full_name(self):
        return self.first_name, self.last_name

    def get_short_name(self):
        return self.first_name

    def create_activation_code(self):
        self.activation_code = str(uuid.uuid4())

    def __str__(self):
        return f"Name: {self.first_name}, email: {self.email}"


class UserProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)

    # autocomplete fields
    image = models.ImageField(null=True, blank=True)
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)
    father_name = models.CharField('father_name', max_length=100)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False, verbose_name='номер телефона')
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    about_self = models.TextField(blank=False, null=True, verbose_name='доп информация')

    def __str__(self):
        return f"Profile-ID: {self.id}, Name: {self.first_name}, email: {self.email}"


class EducationCentreProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)

    # autocomplete fields
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)
    father_name = models.CharField('father_name', max_length=100)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    logo = models.ImageField(null=True, blank=False)
    organization_name = models.CharField(max_length=250, blank=False, null=True)
    description = models.TextField(blank=False, null=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    video = models.CharField(max_length=250, null=True, blank=True)
    address = models.TextField(blank=False, null=True)
    number_of_students = models.PositiveIntegerField(null=True, blank=True)
    verification = models.BooleanField(default=False, blank=True)

    # rate
    number_of_comments = models.PositiveIntegerField(default=0, blank=True)
    sum_of_rate = models.PositiveIntegerField(default=0, blank=True)
    rate = models.FloatField(default=0, blank=True)

    def __str__(self):
        return f"Profile-ID: {self.id}, Manager's name: {self.first_name}, organization: {self.organization_name}"


class TeacherProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)

    # autocomplete fields
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)
    father_name = models.CharField('father_name', max_length=100)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    avatar = models.ImageField(null=True, blank=False)
    description = models.TextField(blank=False, null=True)
    instagram = models.CharField(max_length=250, null=True, blank=True)
    video = models.CharField(max_length=250, null=True, blank=True)
    address = models.CharField(max_length=250, blank=False, null=True)
    number_of_students = models.PositiveIntegerField(null=True, blank=True)
    verification = models.BooleanField(default=False, blank=True)
    work_experience = models.TextField(null=True, blank=False)
    categories = models.ManyToManyField(Category, related_name='categories')
    cost_per_hour = models.PositiveIntegerField(blank=False, null=True)
    time_table = models.CharField(max_length=250, null=True, blank=False)
    lesson_duration = models.CharField(max_length=250, null=True, blank=False)
    education = models.TextField(blank=False, null=True)
    sale = models.CharField(max_length=250, blank=True, null=True)

    # rate
    number_of_comments = models.PositiveIntegerField(default=0, blank=True)
    sum_of_rate = models.PositiveIntegerField(default=0, blank=True)
    rate = models.FloatField(default=0, blank=True)

    def __str__(self):
        return f"Profile-ID: {self.id}, Full name: {self.first_name, self.last_name}"


class NonProfitOrganizationProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)

    # autocomplete fields
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)
    father_name = models.CharField('father_name', max_length=100)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    organization_name = models.CharField(max_length=250, blank=False, null=True)
    description = models.TextField(blank=False, null=True)

    def __str__(self):
        return f"Profile-ID: {self.id}, Name: {self.first_name}," \
               f" non-profit organization name: {self.organization_name}"


class EmployerProfile(models.Model):
    user = models.OneToOneField(AUTH_USER_MODEL, on_delete=models.CASCADE)

    # autocomplete fields
    first_name = models.CharField('first_name', max_length=100)
    last_name = models.CharField('last_name', max_length=100)
    father_name = models.CharField('father_name', max_length=100)
    phone_number = PhoneNumberField(unique=True, null=False, blank=False)
    email = models.EmailField(_('email address'), max_length=255, unique=True)

    organization_name = models.CharField(max_length=250, blank=False, null=True)
    description = models.TextField(blank=False, null=True)

    def __str__(self):
        return f"Profile-ID: {self.id}, Full name: {self.first_name, self.last_name}," \
               f"organization name: {self.organization_name}"
