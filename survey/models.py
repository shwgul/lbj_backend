from django.db import models

# Create your models here.
class Member(models.Model):
    memberId = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    firstName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)