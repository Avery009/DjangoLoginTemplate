from django.db import models

# Create your models here.
class Users(models.Model):
	userID = models.BigAutoField(primary_key=True),
	username = models.CharField(blank=False,null=False,max_length=40)
	password = models.CharField(blank=False,null=False,max_length=40)
