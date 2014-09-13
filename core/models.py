from autoslug import AutoSlugField
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey, CharField, TextField, DateTimeField, BooleanField
from positions.fields import PositionField
# --- Profile ---
from eathub import settings


class Profile(AbstractUser):
    display_name = models.CharField(max_length=50, blank=False)
    modification_date = models.DateTimeField(null=True)
    language = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    website = models.URLField(null=True)
    location = models.CharField(max_length=50, null=True)

    def __unicode__(self):
        return str(self.display_name)


# --- Recipe ---
class Recipe(models.Model):
    slug = AutoSlugField(populate_from='title', unique_with='author')
    title = CharField(max_length=50, blank=False)
    description = TextField(blank=False)
    author = ForeignKey(settings.AUTH_USER_MODEL, related_name='recipes')
    main_image = models.ImageField(upload_to="images/recipe/", null=False)
    serves = CharField(max_length=50, blank=False)
    time = models.CharField(max_length=50)
    notes = TextField(null=True)
    language = CharField(max_length=50, blank=False)

    #TODO definir estado mediante un enum
    is_published = BooleanField(default=False)
    is_draft = BooleanField(default=True)

    updated = DateTimeField(auto_now=True, null=True)
    created = DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.title


class Step(models.Model):
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to="images/recipe/", null=True, blank=True)
    recipe = models.ForeignKey(Recipe, related_name='steps')
    position = PositionField(collection='recipe')

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return "(%s) %s" % (self.position, self.text)


class Ingredient(models.Model):
    text = models.CharField(max_length=100, blank=False)
    recipe = models.ForeignKey(Recipe, related_name='ingredients')
    position = PositionField(collection='recipe')

    class Meta:
        ordering = ['position']

    def __unicode__(self):
        return self.text
