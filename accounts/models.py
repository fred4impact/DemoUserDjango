from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.db import models 
import datetime

from .managers import CustomUserManager

# Create your models here.
class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email'),max_length=60,unique=True)
    name = models.CharField( _('Name') ,max_length=100)
    city = models.CharField(_('your city') ,max_length=100)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    date_joined = models.DateTimeField(default=timezone.now)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [ 'name','city','password']

    objects = CustomUserManager()
    

    def __str__(self):
      return self.email


    def  has_perm(self, perm, obj=None):
       return self.is_admin


    def has_model_perms(self, app_label):
       return true 
