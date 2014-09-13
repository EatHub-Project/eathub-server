from core.models import Profile, Recipe
from django.db import models
from positions.fields import PositionField
# --- Profile ---

# Create your models here.


class GenericFood(models.Model):
    name = models.CharField(max_length=20, blank=False)

    def __str__(self):
        return self.name


class ItemRequirement(models.Model):
    name = models.CharField(max_length=20, blank=False)
    generic_food = models.ForeignKey(GenericFood, related_name='item_requirements')

    def __str__(self):
        return self.name


class DayPlan(models.Model):
    date = models.DateField()
    user = models.ForeignKey(Profile)

    def __str__(self):
        return "%s %s" % (self.date, self.user.username)


class Meal(models.Model):
    name = models.CharField(max_length=20, blank=False)
    position = PositionField(collection="user_day")
    #TODO tag
    user_day = models.ForeignKey(DayPlan, related_name='meals')
    recipe = models.ForeignKey(Recipe, null=True, blank=True)
    generic_foods = models.ManyToManyField(GenericFood, null=True, blank=True)

    def __str__(self):
        return self.name
