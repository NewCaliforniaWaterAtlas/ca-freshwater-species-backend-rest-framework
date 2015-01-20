from api.models import Element, AuVElm
from api.serializers import ElementSerializer, AuVElmSerializer
from rest_framework import generics


class ElementList(generics.ListAPIView):
    """
    List all elements.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class ElementDetail(generics.RetrieveAPIView):
    """
    Retrieve a single element.
    """
    queryset = Element.objects.all()
    serializer_class = ElementSerializer


class AuvelmList(generics.ListAPIView):
    """
    List all elements.
    """
    queryset = AuVElm.objects.all()
    serializer_class = AuVElmSerializer


class AuvelmDetail(generics.RetrieveAPIView):
    """
    Retrieve a single auvelm.
    """
    queryset = AuVElm.objects.all()
    serializer_class = AuVElmSerializer
