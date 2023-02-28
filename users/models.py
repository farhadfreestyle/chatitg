from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    first_name = models.CharField(max_length=30, default='chatitg')
    last_name = models.CharField(max_length=30, default='chatitg')
    profile_picture = models.FileField(default='static/images/Profile_picture/pp.jpg', upload_to='static/images/Profile_picture/')
    username = models.CharField(max_length=30, unique=True)
    email = models.EmailField(unique=True)
    phone = models.CharField(null=True, max_length=30)
    is_active = models.BooleanField(default=True, null=True)
    last_login = models.DateField(null = True)
    is_staff = models.BooleanField(default=False) # a admin user; non super-user
    admin = models.BooleanField(default=False) # a superuser
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'username']
    


    def __str__(self):
        return self.email  

  
    
    
    
    class Meta:
        verbose_name= 'User'
        verbose_name_plural = 'Users'
        
