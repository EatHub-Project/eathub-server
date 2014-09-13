from organizer.models import GenericFood, ItemRequirement, DayPlan, Meal
from rest_framework import serializers


class ItemRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRequirement
        fields = ['name']


class GenericFoodSerializer(serializers.ModelSerializer):
    item_requirements = ItemRequirementSerializer(many=True)

    class Meta:
        model = GenericFood


class MealSerializer(serializers.ModelSerializer):
    generic_foods = GenericFoodSerializer(many=True)
    
    class Meta:
        model = Meal
        fields = ['name', 'recipe', 'generic_foods']


class DayPlanSerializer(serializers.ModelSerializer):
    meals = MealSerializer(many=True)

    class Meta:
        model = DayPlan