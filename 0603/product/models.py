from msilib.schema import Class
from unicodedata import category
from django.db import models

# Create your models here.
class Drink(models.Model):
    class Meta:
        db_table = "Drink"

    name = models.CharField(max_length=256)
    caregoty =  models.CharField
    nutrition_facts = models.TextField()
    allergy = models.TextField()

class Category(models.Model):
    class Meta:
        db_table = "Category"


    Category_name =  models.OneToManyField('Drink')
    drink = models.ForeignKey(Drink)

Class