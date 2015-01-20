from rest_framework import serializers
from api.models import *


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = (
            'group_field',
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
            'sourcegrp_name',
            'use_agree',
            'permission_request_needed',
            'permission_contact_name',
            'permission_contact_email',
            'permission_status',
            'permission',
            'comment_id',
            'citation',
            'weblink',
            'pre_release_review',
            'aggregator',
            'count_huc12s',
            'count_elm_ids',
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
