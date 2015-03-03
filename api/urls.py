from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from rest_framework.urlpatterns import format_suffix_patterns
from api import settings, views

urlpatterns = patterns('',
    url(r'^elements/$', views.ElementList.as_view()),
    url(r'^elements/(?P<pk>[0-9]+)/$', views.ElementDetail.as_view()),
    url(r'^auvelm/$', views.AuvelmList.as_view()),
    url(r'^auvelm/(?P<pk>[0-9]+)/$', views.AuvelmDetail.as_view()),
    url(r'^huc12sz6/$', views.Huc12_Z6List.as_view()),
    url(r'^huc12sz6/(?P<pk>[0-9]+)/$', views.Huc12_Z6Detail.as_view()),
    url(r'^huc12sz7/$', views.Huc12_Z7List.as_view()),
    url(r'^huc12sz7/(?P<pk>[0-9]+)/$', views.Huc12_Z7Detail.as_view()),
    url(r'^huc12sz8/$', views.Huc12_Z8List.as_view()),
    url(r'^huc12sz8/(?P<pk>[0-9]+)/$', views.Huc12_Z8Detail.as_view()),
    url(r'^huc12sz9/$', views.Huc12_Z9List.as_view()),
    url(r'^huc12sz9/(?P<pk>[0-9]+)/$', views.Huc12_Z9Detail.as_view()),
    url(r'^huc12sz10/$', views.Huc12_Z10List.as_view()),
    url(r'^huc12sz10/(?P<pk>[0-9]+)/$', views.Huc12_Z10Detail.as_view()),
    url(r'^huc12sz11/$', views.Huc12_Z11List.as_view()),
    url(r'^huc12sz11/(?P<pk>[0-9]+)/$', views.Huc12_Z11Detail.as_view()),
    url(r'^huc12sz12/$', views.Huc12_Z12List.as_view()),
    url(r'^huc12sz12/(?P<pk>[0-9]+)/$', views.Huc12_Z12Detail.as_view()),
    url(r'^huc12sz13/$', views.Huc12_Z13List.as_view()),
    url(r'^huc12sz13/(?P<pk>[0-9]+)/$', views.Huc12_Z13Detail.as_view()),
    url(r'^huc12sz14/$', views.Huc12_Z14List.as_view()),
    url(r'^huc12sz14/(?P<pk>[0-9]+)/$', views.Huc12_Z14Detail.as_view()),
    url(r'^huc12sz15/$', views.Huc12_Z15List.as_view()),
    url(r'^huc12sz15/(?P<pk>[0-9]+)/$', views.Huc12_Z15Detail.as_view()),

    url(r'^species/$', views.SpeciesList.as_view()),
    ) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
