from api.api_organizer.serializers import GenericFoodSerializer
from organizer.models import GenericFood
from rest_framework import viewsets


class GenericFoodViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = GenericFood.objects.all()
    serializer_class = GenericFoodSerializer