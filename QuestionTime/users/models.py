from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    '''
    Custom user that extends AbstractUser class.
    '''
    pass
