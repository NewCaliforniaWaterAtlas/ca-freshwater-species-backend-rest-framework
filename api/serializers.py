from rest_framework import serializers
from api.models import *


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = (
            'listed',
            'vulnerable',
            'group_field',
            'elm_comnam',
            'elm_scinam',
            'elm_scin_1',
            'elm_scin_2',
            'elm_scin_3',
            'elm_scin_4',
            'endemic',
            'vulnerable',
            'endemic'
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
            'pre_release_review',
        )

class AuVElmSerializer(serializers.ModelSerializer):
    element = ElementSerializer(read_only=True)
    observation_type = ObservationTypeSerializer(read_only=True)
    source = SourceSerializer(read_only=True)

    class Meta:
        model = AuVElm
        fields = (
            'id',
            'element',
            'huc_12',
            'observation_type',
            'source',
            'frequency',
            'sum_amount',
        )
