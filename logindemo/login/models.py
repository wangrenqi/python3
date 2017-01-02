from __future__ import unicode_literals

from django.db import models

# Create your models here.


class AuthCode(models.Model):
    create_time  = models.CharField(max_length=300)
    random_code = models.CharField(max_length=30)

class Auth(models.Model):
    create_time = models.FloatField()
    random_code = models.CharField(max_length=50)
    def __str__(self):
        return u'%s' % self.create_time 
        #fake: 1483353551.19
        #real: 1483353551.190901
    
    

# class Per(models.Model):
#     name = models.CharField(max_length=30)
#     age = models.FloatField()
