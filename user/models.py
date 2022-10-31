from django.db import models
from django.contrib.auth.models import User

class Profession(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    prof_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

class InfoUser(models.Model):
    country = models.CharField(max_length=100)
    language = models.CharField(max_length=100)
    gender = models.CharField(max_length=50)
    about_yourself = models.TextField()
    info_id = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.country


# class NewUser(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     email = models.EmailField(unique=True)
#     password = models.CharField(max_length=50)
#
#     def __str__(self):
#         return self.first_name
