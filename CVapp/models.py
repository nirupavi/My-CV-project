from django.db import models

# Create your models here.



class Resume(models.Model):
    name = models.CharField(max_length=100,unique=True)
    email = models.EmailField(max_length=100)
    mobile = models.PositiveIntegerField()
    locality = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    pin = models.PositiveIntegerField()
    state = models.CharField(max_length=100)
    School = models.CharField(max_length=200)
    School_marks = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    Degree = models.CharField(max_length=200)
    University = models.CharField(max_length=200)
    Degree_percentage = models.DecimalField(blank=True, null=True, max_digits=10, decimal_places=2)
    previous_roll = models.CharField(max_length=100)
    previous_experience = models.CharField(max_length=20)
    Tech_skill = models.CharField(max_length=100)
    job_city = models.CharField(max_length=50)
    profile_image = models.ImageField(upload_to='profileimg', blank=True)
    file = models.FileField(upload_to='doc',blank=True)


    def __str__(self):
        return self.name