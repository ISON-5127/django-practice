from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __unicode__(self):
        return self.username

class Balance(models.Model):
    user = models.CharField(max_length=50)
    balance = models.IntegerField(max_length=50)

    def __unicode__(self):
        return self.user
# class Result(models.Model):
#     result