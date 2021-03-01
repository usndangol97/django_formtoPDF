from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)

    bio = models.TextField()
    language = models.CharField(max_length=100)
    intrest = models.CharField(max_length=100)
    #education
    college_name = models.CharField(max_length=100)
    degree_name = models.CharField(max_length=100)
    degree_passed_date = models.DateField()

    
    #experience
    job_title = models.CharField(max_length=100)
    job_date = models.DateField()
    company_name = models.CharField(max_length=100)
    company_address = models.CharField(max_length=100)
    job_description = models.TextField()

    skill = models.CharField(max_length=100)
    certification = models.CharField(max_length=200)

    def __str__(self):
        return self.name