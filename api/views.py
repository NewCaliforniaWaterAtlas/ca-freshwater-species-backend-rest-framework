import django_filters
from api.models import Element, AuVElm
from api.serializers import ElementSerializer, AuVElmSerializer, SpeciesSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView


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
