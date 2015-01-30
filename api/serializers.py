from rest_framework import serializers
from api.models import Element, ObservationType, Source, AuVElm


class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Element
        fields = (
            'id',
            'scientific_name',
            'alt_scientific_names',
            'common_name',
            'taxonomic_group',
            'endemic',
            'vulnerable',
            'listed',
        )

class ObservationTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ObservationType
        fields = (
            'name',
            'range_obs',
            'current_other',
            'observation_group',
        )

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'name',
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

class SpeciesSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            obj.id: {
                'scientific_name': obj.scientific_name,
                'alt_scientific_names': obj.alt_scientific_names(),
                'common_name': obj.common_name,
                'taxonomic_group': obj.taxonomic_group,
                'endemic': obj.endemic,
                'vulnerable': obj.vulnerable,
                'listed': obj.listed,
            }
        }
