from django.db import models
# Create your models here.
class Member(models.Model):
    memberId = models.CharField(max_length=200,primary_key=True)
    firstName = models.CharField(max_length=200)
    lastName = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    memberType = models.CharField(max_length=4)
    address = models.CharField(max_length=200)
    income = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    homeValue = models.BigIntegerField()
    squareFootage = models.BigIntegerField()
    adoption = models.CharField(max_length=200)
    latitude = models.DecimalField(max_digits=20, decimal_places=10)
    longitude = models.DecimalField(max_digits=20, decimal_places=10)

class Relation(models.Model):
    id = models.AutoField(primary_key=True)
    sunId = models.CharField(max_length=200)
    friendId = models.CharField(max_length=200)
    trustLevel = models.BigIntegerField()
    frequency = models.CharField(max_length=200)
    conversationTopic = models.CharField(max_length=200)
    actualRingLevel = models.BigIntegerField()
