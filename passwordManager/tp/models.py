from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.
class Site(models.Model):
    name = models.CharField(max_length=24)
    identifier = models.CharField(max_length=80)
    password = models.CharField(max_length=80, validators=[MinLengthValidator(11)])
    url = models.IntegerField()
