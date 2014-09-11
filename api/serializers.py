from core.models import Profile, Recipe, Step
from rest_framework import serializers


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields = ('url', 'username', 'display_name', 'email', 'groups')


# --- Recipes ---

class StepSerializer(serializers.ModelSerializer):
    class Meta:
        model = Step
        fields = ['order', 'text', 'image']


class RecipeSerializer(serializers.ModelSerializer):
    steps = StepSerializer(many=True)

    class Meta:
        model = Recipe

