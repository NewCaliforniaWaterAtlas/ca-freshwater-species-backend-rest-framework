import django_filters
from api.models import Element, AuVElm, Huc12
from api.serializers import *
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_gis.filters import InBBoxFilter

class ElementFilter(django_filters.FilterSet):
    """
    Provide the ability to filter on a group, or whether an element is listed or vulnerable.
    """
    class Meta:
        model = Element
        fields = ['taxonomic_group', 'listed', 'vulnerable']


class ElementList(generics.ListAPIView):
    """
    List all elements.

    May be filtered by `taxonomic_group`, e.g., 'Fishes', 'Mammals', etc.

    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer
    filter_class = ElementFilter


class ElementDetail(generics.RetrieveAPIView):
    """
    Retrieve a single element.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class AuvelmFilter(django_filters.FilterSet):
    """
    Provide the ability to filter on a group.
    """
    taxonomic_group = django_filters.CharFilter(name="element__taxonomic_group")
    listed = django_filters.CharFilter(name="element__listed")
    vulnerable = django_filters.CharFilter(name="element__vulnerable")

    class Meta:
        model = AuVElm
        fields = ['taxonomic_group', 'listed', 'vulnerable']


class AuvelmList(generics.ListAPIView):
    """
    List all elements.
    """
    queryset = AuVElm.objects.all()
    serializer_class = AuVElmSerializer
    filter_class = AuvelmFilter


class AuvelmDetail(generics.RetrieveAPIView):
    """
    Retrieve a single auvelm.
    """
    queryset = AuVElm.objects.all()
    serializer_class = AuVElmSerializer


class SpeciesList(APIView):
    """
    List all species.
    """
    def get(self, request, format=None):
        species = Element.objects.all()
        serializer = SpeciesSerializer(species, many=True)
        return Response(dict(species=serializer.data))


class Huc12_Z6List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ6Serializer
    bbox_filter_field = 'z6'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z6Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ6Serializer


class Huc12_Z7List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ7Serializer
    bbox_filter_field = 'z7'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z7Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ7Serializer


class Huc12_Z8List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ8Serializer
    bbox_filter_field = 'z8'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z8Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ8Serializer


class Huc12_Z9List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ9Serializer
    bbox_filter_field = 'z9'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z9Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ9Serializer


class Huc12_Z10List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ10Serializer
    bbox_filter_field = 'z10'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z10Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ10Serializer


class Huc12_Z11List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ11Serializer
    bbox_filter_field = 'z11'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z11Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ11Serializer


class Huc12_Z12List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ12Serializer
    bbox_filter_field = 'z12'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z12Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ12Serializer


class Huc12_Z13List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ13Serializer
    bbox_filter_field = 'z13'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z13Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ13Serializer


class Huc12_Z14List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ14Serializer
    bbox_filter_field = 'z14'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z14Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ14Serializer


class Huc12_Z15List(generics.ListAPIView):
    """
    List all HUC12s.

    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ15Serializer
    bbox_filter_field = 'z15'
    filter_backends = (InBBoxFilter,)
    bbox_filter_include_overlapping = True


class Huc12_Z15Detail(generics.RetrieveAPIView):
    """
    Retrieve a single HUC12.
    """
    queryset = Huc12.objects.all()
    serializer_class = Huc12sZ15Serializer


