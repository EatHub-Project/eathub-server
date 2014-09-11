from core.models import Profile, Recipe, Step, Ingredient
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Profile, UserAdmin)


class StepInline(admin.StackedInline):
    model = Step
    extra = 1


class IngredientInline(admin.TabularInline):
    model = Ingredient
    fields = ['text']
    extra = 3


class RecipeAdmin(admin.ModelAdmin):
    inlines = [IngredientInline, StepInline]


admin.site.register(Recipe, RecipeAdmin)