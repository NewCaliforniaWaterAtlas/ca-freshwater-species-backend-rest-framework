from rest_framework import serializers
from rest_framework_gis.serializers import GeoFeatureModelSerializer
from api.models import Element, ObservationType, Source, AuVElm, Huc12


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


class TaxonomicGroupsSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return {
            'name': obj.name,
            'count': obj.count,
        }


class Huc12sBySpeciesSerializer(serializers.BaseSerializer):
    def to_representation(self, obj):
        return obj.huc_12


class Huc12sZ6Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z6'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z6',
        )


class Huc12sZ7Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z7'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z7',
        )


class Huc12sZ8Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z8'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z8',
        )


class Huc12sZ9Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z9'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z9',
        )


class Huc12sZ10Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z10'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z10',
        )


class Huc12sZ11Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z11'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z11',
        )


class Huc12sZ12Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z12'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z12',
        )


class Huc12sZ13Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z13'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z13',
        )


class Huc12sZ14Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z14'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z14',
        )


class Huc12sZ15Serializer(GeoFeatureModelSerializer):
    class Meta:
        model = Huc12
        geo_field = 'z15'

        fields = (
            'huc_12',
            'first_hu_1',
            'hr_name',
            'z15',
        )


