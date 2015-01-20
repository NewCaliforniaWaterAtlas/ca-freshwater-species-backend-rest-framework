from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from api import settings, views

urlpatterns = patterns('',
    url(r'^elements/$', views.ElementList.as_view()),
    url(r'^elements/(?P<pk>[0-9]+)/$', views.ElementDetail.as_view()),
    url(r'^auvelm/$', views.AuvelmList.as_view()),
    url(r'^auvelm/(?P<pk>[0-9]+)/$', views.AuvelmDetail.as_view()),
    url(r'^docs/', include('rest_framework_swagger.urls')),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
