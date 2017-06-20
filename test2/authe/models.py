from __future__ import unicode_literals
from django.db import models
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# Create your models here.


class questions(models.Model):
    q_name = models.CharField(max_length=100)
    question = models.TextField()
    user = models.TextField()
    id = models.AutoField(primary_key=True)
    result = models.TextField(max_length=300)
    date = models.DateField()



class QUser(models.Model):

    username = models.CharField(primary_key=True, max_length=50)
    password = models.CharField(max_length=200)
    email = models.EmailField(max_length=255, null=True)

    def __str__(self):
        return self.username

class Answer(models.Model):
    user = models.TextField()
    answer = models.TextField()
    date = models.DateField()
    qid = models.IntegerField()
    id = models.AutoField(primary_key=True)

    def __str__(self):
        return self.user


