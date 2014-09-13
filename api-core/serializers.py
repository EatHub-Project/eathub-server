from core.models import Profile, Recipe, Step, Ingredient
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'username', 'display_name', 'email', 'groups')


# --- Recipes ---

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['position', 'text', 'image']


class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = ['position', 'text']


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)
    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Recipe

