from rest_framework import serializers
from api.models import *


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = (
            'elm_id',
            'elm_scinam',
            'elm_scin_1',
            'elm_scin_2',
            'elm_scin_3',
            'elm_scin_4',
            'elm_comnam',
            'group_field',
            'endemic',
            'vulnerable',
            'listed',
        )

class ObservationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservationType
        fields = (
            'obs_typ_name',
            'range_obs',
            'current_other',
        )

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'source_name',
            'citation',
            'weblink',
        )

class AuVElmSerializer(serializers.ModelSerializer):
    element = ElementSerializer(read_only=True)
    observation_type = ObservationTypeSerializer(read_only=True)
    source = SourceSerializer(read_only=True)

    class Meta:
        model = AuVElm
        fields = (
            'element',
            'huc_12',
            'observation_type',
            'source',
            'frequency',
            'sum_amount',
        )
