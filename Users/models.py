from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models
from django.utils import timezone
# Create your models here.

class CustomUserManager(BaseUserManager):
    def _create_user(self,documentNumber, fullName, email, password, **extra_fields):
        if not email:
            raise ValueError('No has diligenciado una direccion de correo electronico adecuada')

        email = self.normalize_email(email)
        user = self.model(documentNumber, fullName, email = email, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)

        return user
    
    def create_user(self, documentNumber = None, fullName = None, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(documentNumber, fullName ,email, password, **extra_fields)
    
    def create_superuser(self, documentNumber = None, fullName = None, email = None, password = None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        
        return self._create_user(documentNumber, fullName ,email, password, **extra_fields)
    
class User(AbstractBaseUser, PermissionsMixin):
    documentNumber = models.CharField(primary_key = True ,max_length = 10, blank = True, default = '', unique = True, verbose_name = 'Document Number')
    fullName = models.CharField(max_length = 100, verbose_name = 'Full Name')
    email = models.EmailField(verbose_name = 'User Email', unique = True)
    password = models.CharField(max_length = 20 ,verbose_name = 'User Password')
    
    is_active = models.BooleanField(default = True)
    is_superuser = models.BooleanField(default = False)
    is_staff = models.BooleanField(default = False)

    date_joined = models.DateTimeField(default = timezone.now)
    last_login = models.DateTimeField(blank = True, null = True)

    objects = CustomUserManager()

    USERNAME_FIELD = 'documentNumber'
    EMAIL_FIELD = 'email'
    PASSWORD_FIELD = 'password'
    REQUIRED_FIELDS = ['fullName', 'email', 'password']

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'