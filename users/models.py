from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
# Create your models here.


class UserManager(BaseUserManager):
    
    use_in_migrations = True

    def _create_user(self,email,password,**extra_fields):
        if not email:
            raise ValueError("You need to set the email")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email,password,**extra_fields)

        
    def createsuperuser(self,email,password,**extra_fields):
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)

        if extra_fields.get('is_staff') != True:
            raise ValueError('super user must is_staff=True')
        
        if not extra_fields.get('is_superuser') != True:
            raise ValueError('superuser must have is_superuser=True')

        return self._create_user(email, password, **extra_fields)
        

class User(AbstractUser):
    username=None
    email = models.EmailField('email_address', unique=True,default=' ')
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='users_user_permissions' #added related name to user_permissions
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='users_user_groups'  # Add related_name argument for groups
    )

        
    objects = UserManager()


    
