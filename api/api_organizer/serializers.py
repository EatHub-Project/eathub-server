from organizer.models import GenericFood, ItemRequirement
from rest_framework import serializers


class ItemRequirementSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemRequirement
        fields = ['name']


class GenericFoodSerializer(serializers.ModelSerializer):
    item_requirements = ItemRequirementSerializer(many=True)

    class Meta:
        model = GenericFood
