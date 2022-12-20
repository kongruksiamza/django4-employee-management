from django.db import models

# Create your models here.
class Employee(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    address = models.TextField()
    gender = models.CharField(
        max_length=6,
        choices=[('ชาย','ชาย'),('หญิง','หญิง')],
        default='ชาย'
    )
    birthdate=models.DateField()
    department=models.CharField(
        max_length=50,
        choices=[('กราฟิก','กราฟิก'),('ไอที','ไอที'),('บัญชี','บัญชี')],
        default='กราฟิก'
    )
    salary = models.IntegerField()
    cover = models.ImageField(upload_to="images",blank=True)