# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.contrib.gis.db import models


class Origin(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(blank=False, null=False)

    class Meta:
        managed = False
        db_table = 'origins'

    def __unicode__(self):
        return '%s' % self.name


class ObservationType(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True)
    range_obs = models.CharField(blank=True)
    current_other = models.CharField(blank=True)
    observation_group = models.CharField(blank=True)

    class Meta:
        managed = False
        db_table = 'observation_types'

    def __unicode__(self):
        return '%s' % self.name


class Source(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(unique=True)
    sourcegrp_name = models.CharField(blank=True)
    use_agreement = models.TextField(blank=True)
    permission_request_needed = models.CharField(blank=True)
    permission_contact_name = models.CharField(blank=True)
    permission_contact_email = models.CharField(blank=True)
    permission_status = models.TextField(blank=True)
    permission_scale = models.CharField(blank=True)
    comment_id = models.IntegerField(blank=True, null=True)
    citation = models.TextField(blank=True)
    weblink = models.CharField(blank=True)
    pre_release_review = models.CharField(blank=True)
    aggregator = models.CharField(blank=True)
    count_huc12s = models.IntegerField(blank=True, null=True)
    count_elm_ids = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sources'

    def __unicode__(self):
        return '%s' % self.name


class HabitatUsage(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(blank=True)

    class Meta:
        managed = False
        db_table = 'habitat_usages'

    def __unicode__(self):
        return '%s' % self.name


class Element(models.Model):
    id = models.BigIntegerField(primary_key=True)
    scientific_name = models.CharField(blank=True)
    common_name = models.CharField(blank=True)
    taxonomic_group = models.CharField(db_index=True)
    fwa_v1 = models.IntegerField(blank=True, null=True)
    tax_list = models.CharField(blank=True)
    g_rank = models.CharField(blank=True)
    s_rank = models.CharField(blank=True)
    elm_scin_1 = models.CharField(blank=True)
    elm_scin_2 = models.CharField(blank=True)
    elm_scin_3 = models.CharField(blank=True)
    elm_scin_4 = models.CharField(blank=True)
    kingdom = models.CharField(blank=True)
    phylum = models.CharField(blank=True)
    tax_class = models.CharField(blank=True)
    tax_order = models.CharField(blank=True)
    family = models.CharField(blank=True)
    genus = models.CharField(blank=True)
    species = models.CharField(blank=True)
    subsp_var = models.CharField(blank=True)
    kingdom_id = models.CharField(blank=True)
    phylum_id = models.CharField(blank=True)
    tax_class_i = models.CharField(blank=True)
    tax_order_i = models.CharField(blank=True)
    family_id = models.CharField(blank=True)
    genus_id = models.CharField(blank=True)
    species_id = models.CharField(blank=True)
    other_id = models.CharField(blank=True)
    sensitive_fam = models.CharField(blank=True)
    ns_endemic = models.IntegerField(blank=True, null=True)
    safit_endemic = models.IntegerField(blank=True, null=True)
    other_endemic = models.IntegerField(blank=True, null=True)
    endemism_comment = models.TextField(blank=True)
    fed_list = models.CharField(blank=True)
    state_list = models.CharField(blank=True)
    other_list = models.CharField(blank=True)
    mgtag_list = models.CharField(blank=True)
    listed = models.NullBooleanField()
    vulnerable = models.NullBooleanField()
    endemic = models.NullBooleanField()
    common = models.NullBooleanField()
    not_evaluated = models.NullBooleanField()
    extinct = models.NullBooleanField()

    class Meta:
        managed = False
        db_table = 'elements'

    def __unicode__(self):
        return '%s/%s' % (self.scientific_name, self.common_name)

    def alt_scientific_names(self):
        asn = ''
        if self.elm_scin_1:
            asn += '%s, ' % self.elm_scin_1
        if self.elm_scin_2:
            asn += '%s, ' % self.elm_scin_2
        if self.elm_scin_3:
            asn += '%s, ' % self.elm_scin_3
        if self.elm_scin_4:
            asn += '%s' % self.elm_scin_4
        return asn.rstrip(', ')

class AuVElm(models.Model):
    id = models.BigIntegerField(primary_key=True)
    element = models.ForeignKey(Element, to_field='id', db_column='elm_id')
    huc_12 = models.CharField(blank=True)
    observation_type = models.ForeignKey(ObservationType, to_field='id', db_column='obs_typ_id')
    source = models.ForeignKey(Source, to_field='id', db_column='source_id')
    frequency = models.FloatField(blank=True, null=True)
    sum_amount = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'au_v_elms'

    def __unicode__(self):
        return '%s: %s' % (self.huc_12, self.element)


class Huc12(models.Model):
    gid = models.IntegerField()
    huc_12 = models.CharField(primary_key=True)
    first_huc8 = models.CharField()
    first_hu_1 = models.CharField()
    shape_leng = models.FloatField()
    shape_area = models.FloatField()
    area_ha = models.IntegerField()
    hr_name = models.CharField()
    geom = models.MultiPolygonField()
    topogeom = models.MultiPolygonField() # this is not right
    z6 = models.MultiPolygonField()
    z7 = models.MultiPolygonField()
    z8 = models.MultiPolygonField()
    z9 = models.MultiPolygonField()
    z10 = models.MultiPolygonField()
    z11 = models.MultiPolygonField()
    z12 = models.MultiPolygonField()
    z13 = models.MultiPolygonField()
    z14 = models.MultiPolygonField()
    z15 = models.MultiPolygonField()
    objects = models.GeoManager()

    class Meta:
        managed = False
        db_table = 'huc12s'


class TaxonomicGroup:
    def __init__(self, id, name, count):
        self.id = id
        self.name = name
        self.count = count

