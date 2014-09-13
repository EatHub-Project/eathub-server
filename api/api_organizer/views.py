from api.api_organizer.serializers import GenericFoodSerializer, DayPlanSerializer
from organizer.models import GenericFood, DayPlan
from rest_framework import viewsets


class GenericFoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GenericFood.objects.all()
    serializer_class = GenericFoodSerializer


class DayPlanViewSet(viewsets.ModelViewSet):
    queryset = DayPlan.objects.all()
    serializer_class = DayPlanSerializer

