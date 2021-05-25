from hospital.models import Hospital
from django.db import models

# Create your models here.
class Doctor(models.Model):
    class Meta:
        db_table = "Doctor"

    Doctor_ID = models.CharField(max_length=20, primary_key=True)
    Password = models.CharField(max_length=12)
    Name = models.CharField(max_length=50)
    Age = models.IntegerField()
    Gender = models.CharField(max_length=10)
    Aadhaar_ID = models.CharField(max_length=12)
    Mobile_No = models.CharField(max_length=12)
    Email = models.TextField()
    Reg_No_MCI = models.CharField(max_length=10)
    Qualification = models.TextField()
    Area_of_Specialisation = models.CharField(max_length=30)
    Year_of_Experience = models.IntegerField()
    Type_of_Practice = models.CharField(max_length=20)
    Designation = models.CharField(max_length=50)
    Hospital_ID = models.ForeignKey(Hospital,on_delete=models.CASCADE)
    Photo = models.ImageField(upload_to="doctor_profile", null=True, blank=True)

    def __str__(self):
        return self.Name
