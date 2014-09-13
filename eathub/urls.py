# coding=utf-8
from django.conf.urls import patterns, include, url
from django.contrib import admin
from eathub import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eathub.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('api.urls')),

)



# Solución a los estáticos en Heroku
# Mil gracias: http://stackoverflow.com/questions/9047054/heroku-handling-static-files-in-django-app
# if settings.DEBUG ??
urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
    )