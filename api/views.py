import django_filters
from api.models import Element, AuVElm
from api.serializers import ElementSerializer, AuVElmSerializer
from rest_framework import generics


class ElementFilter(django_filters.FilterSet):
    """
    Provide the ability to filter on a group, or whether an element is listed or vulnerable.
    """
    group = django_filters.CharFilter(name="group_field")

    class Meta:
        model = Element
        fields = ['group', 'listed', 'vulnerable']


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
    group = django_filters.CharFilter(name="element__group_field")
    listed = django_filters.CharFilter(name="element__listed")
    vulnerable = django_filters.CharFilter(name="element__vulnerable")

    class Meta:
        model = AuVElm
        fields = ['group', 'listed', 'vulnerable']


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
