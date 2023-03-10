from django.db import models

# Create your models here.
work_type = (('plumber', 'PLUMBER'),
             ('carpenter', 'CARPENTER'),
             ('labour', 'LABOUR'),
             )
loc = (
    ('mumbai', 'MUMBAI'),
    ('thane', 'THANE'),
    ('pune', 'PUNE'),
)

lang = (
    ('english', 'ENGLISH'),
    ('hindi', 'HINDI'),
    ('marathi', 'MARATHI'),
)


class Workers(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()
    gender = models.CharField(max_length=100)
    email = models.EmailField()
    photo = models.ImageField(null=False, blank=False)
    phone = models.CharField(max_length=10)
    Address = models.TextField()
    Adhaarcard = models.ImageField(null=False, blank=False)
    cityoforigin = models.CharField(max_length=20)
    medicalhistory = models.TextField()
    skills = models.CharField(max_length=100, choices=work_type, default=None)
    prefferedworklocation = models.CharField(
        max_length=100, choices=loc, default=None)
    languages = models.CharField(max_length=100, choices=lang, default=None)
