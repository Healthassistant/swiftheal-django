from django.db import models

# Create your models here.
class Hospital(models.Model):
    class Meta:
        db_table = "Hospital"

    ID = models.CharField(max_length=10,primary_key=True)
    Name = models.TextField()
    Address = models.TextField()
    City = models.CharField(max_length=20)
    State = models.CharField(max_length=20)
    Pincode = models.CharField(max_length=6)
    Late_Fine = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Name