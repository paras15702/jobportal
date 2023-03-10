from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Job(models.Model):

    Job_id = models.AutoField(primary_key=True)
    Job_location = models.CharField(max_length=100)
    Language_preferences = models.CharField(max_length=20, choices=(()))
    Wages_per_hour = models.IntegerField(MinValueValidator(2000))
    Contract_tenure = models.DurationField()
    required_skills = models.TextField()
    Job_status = models.BooleanField(default=False)
    Employer_contact_number = models.CharField(max_length=20, blank=False)
    Number_of_vacancies = models.PositiveIntegerField(MinValueValidator(0))


class EmployerModel(models.Model):
    emp_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    password = models.IntegerField(max_length=8)
    pfp = models.ImageField(null=False, blank=False)
    aadharcard = models.ImageField(null=False, blank=False)

    def _str_(self):
        return self.emp_id + "" + str(self.name)
