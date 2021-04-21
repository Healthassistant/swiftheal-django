from django.db import models

# Create your models here.
class User(models.Model):
    class Meta:
        db_table = 'User'
    name = models.CharField(max_length=25)