from django.db import models
from django.contrib.auth.models import User

class Home(models.Model):
    author = models.ForeignKey(User, on_delete = models.CASCADE)
    clubname = models.CharField('clubname', max_length=20)
    kakaoid = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=12)
    use = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    body = models.TextField()
    

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]