from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('api.api_core.urls')),
    url(r'organizer/', include('api.api_organizer.urls')),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]