from django.contrib import admin

# Register your models here.
from organizer.models import GenericFood, Meal, DayPlan, ItemRequirement


class ItemRequirementInline(admin.TabularInline):
    model = ItemRequirement
    fields = ['name']
    extra = 2


class GenericFoodAdmin(admin.ModelAdmin):
    model = GenericFood
    fields = ['name']
    inlines = [ItemRequirementInline]


class MealInline(admin.StackedInline):
    model = Meal
    fields = ['name', 'recipe', 'generic_foods']
    extra = 2


class DayPlanAdmin(admin.ModelAdmin):
    inlines = [MealInline]


admin.site.register(DayPlan, DayPlanAdmin)
admin.site.register(GenericFood, GenericFoodAdmin)