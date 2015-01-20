from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from api import views

urlpatterns = [
    url(r'^elements/$', views.ElementList.as_view()),
    url(r'^elements/(?P<pk>[0-9]+)/$', views.ElementDetail.as_view()),
    url(r'^auvelm/$', views.AuvelmList.as_view()),
    url(r'^auvelm/(?P<pk>[0-9]+)/$', views.AuvelmDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
