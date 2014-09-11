from core.models import Profile, Recipe, Step
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# Register your models here.
admin.site.register(Profile, UserAdmin)


class StepInline(admin.StackedInline):
    model = Step
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    inlines = [StepInline]


admin.site.register(Recipe, RecipeAdmin)