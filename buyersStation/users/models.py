from django.db import models

# Create your models here.
class User(models.Model):
    user_name = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    user_type = models.CharField(max_length= 1,default= 0)

    def __str__(self):
        return self.user_name , self.email