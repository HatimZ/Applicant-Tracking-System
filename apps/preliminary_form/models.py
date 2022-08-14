from django.db import models
from django.forms import CharField



class Resume(models.Model):
   file_data_in_bytes = models.BinaryField(null=True)
   file_name = models.CharField(max_length=50)


class FormEntry(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100)
    experience = models.CharField(max_length=50) #0,1,2,3
    visa_status = models.CharField(max_length=50)  # 0,1
    salary_expect = models.CharField(max_length=50,null=True)
    ph_number = models.CharField(max_length=50,null=True)
    employment_status = models.CharField(max_length=50)
    gender = models.CharField(max_length=50, blank=True)
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, null=True)



