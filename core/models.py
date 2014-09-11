from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models import ForeignKey, CharField, TextField, DateTimeField, BooleanField

# --- Profile ---
from eathub import settings


class Profile(AbstractUser):
    display_name = models.CharField(max_length=50, blank=False)
    modification_date = models.DateTimeField(null=True)
    language = models.CharField(max_length=50)
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True)
    website = models.URLField(null=True)
    location = models.CharField(max_length=50, null=True)

    def __str__(self):
        return str(self.display_name)


# --- Recipe ---
class Recipe(models.Model):
    title = CharField(max_length=50, blank=False)
    description = TextField(blank=False)
    creation_date = DateTimeField(auto_now_add=True)
    main_image = models.ImageField(upload_to="images/recipe/", null=False)
    modification_date = DateTimeField(auto_now_add=True, null=True)
    serves = CharField(max_length=50, blank=False)
    language = CharField(max_length=50, blank=False)
    notes = TextField(null=True)

    #TODO definir estado mediante un enum
    is_published = BooleanField(default=False)
    is_draft = BooleanField(default=True)

    author = ForeignKey(settings.AUTH_USER_MODEL)
    time = models.CharField(max_length=50)

    def __str__(self):
        return self.title


class Step(models.Model):
    text = models.TextField(blank=False)
    image = models.ImageField(upload_to="images/recipe/", null=True, blank=True)
    recipe = models.ForeignKey(Recipe, related_name='steps')
    order = models.IntegerField(blank=False)


