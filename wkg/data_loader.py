#!/usr/bin/env python

#
# Run this from the top level as
#
#    honcho run python wkg/data_loader.py 'subdirectory'
#

import os
import psycopg2
from petl import *
import argparse

# get the subdirectory containing the .csv files from the command line and check that it exists.
#
parser = argparse.ArgumentParser(description='Import .csv files for the Freshwater Species Database.')
parser.add_argument('subdir', help="name of the database subdirectory (expected to be in 'wkg/')")
args = parser.parse_args()
if not os.path.exists(os.path.join('wkg', args.subdir)):
    print('Error: ' + args.subdir + " does not exist as a subdirectory of 'wkg/'.")
    exit()

# Set up the database connection
#
connection = psycopg2.connect(
    database=os.environ['DB'],
    user=os.environ['DB_USER'],
    password=os.environ['DB_PASSWORD'],
    host=os.environ['DB_HOST'],
)
cursor = connection.cursor()

# Origin: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS origins CASCADE;
CREATE TABLE origins (
    id                          INTEGER NOT NULL UNIQUE PRIMARY KEY,
    name                        VARCHAR NOT NULL
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Origin.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'Org_ID':                   'id',
    'Org_Name':                 'name',
})
f = convertnumbers(f)
todb(f, connection, 'origins')

# ObservationType: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS observation_types CASCADE;
CREATE TABLE observation_types (
    id                          INTEGER UNIQUE PRIMARY KEY,
    name                        VARCHAR NOT NULL UNIQUE,
    range_obs                   VARCHAR,
    current_other               VARCHAR,
    observation_group           VARCHAR
);
CREATE INDEX ON observation_types (id);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'ObservationType.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'ObsTyp_ID':                'id',
    'ObsTyp_Name':              'name',
    'Range_Obs':                'range_obs',
    'Current_Other':            'current_other',
    'Group_':                   'observation_group',
})
f = convertnumbers(f)
todb(f, connection, 'observation_types')

# Source: create, map, and load
#
# @todo source_name should be UNIQUE.
cursor.execute("""
DROP TABLE IF EXISTS sources CASCADE;
CREATE TABLE sources (
    id                          INTEGER NOT NULL UNIQUE PRIMARY KEY,
    name                        VARCHAR,
    sourcegrp_name              VARCHAR,
    use_agreement               TEXT,
    permission_request_needed   VARCHAR,
    permission_contact_name     VARCHAR,
    permission_contact_email    VARCHAR,
    permission_status           TEXT,
    permission_scale            VARCHAR,
    comment_id                  INTEGER,
    citation                    TEXT,
    weblink                     VARCHAR,
    pre_release_review          VARCHAR,
    aggregator                  VARCHAR,
    count_huc12s                INTEGER,
    count_elm_ids               INTEGER
);
CREATE INDEX ON sources (id);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Source.csv'))
f = cutout(f, 'Status', 'Permission_notes', 'Duplication', 'Jeanette', 'Source_Name', 'Access_date', 'Sort')
f = rename(f, {
    'Source_ID':                 'id',
    'Source_Name_Full':          'name',
    'SourceGrp_Name':            'sourcegrp_name',
    'Use_agreement':             'use_agreement',
    'Premission_request_needed': 'permission_request_needed',
    'Permission_contact_name':   'permission_contact_name',
    'Permission_contact_email':  'permission_contact_email',
    'Permission_status':         'permission_status',
    'Permission_scale':          'permission_scale',
    'Comment_ID':                'comment_id',
    'Citation':                  'citation',
    'Weblink':                   'weblink',
    'Pre_release_review':        'pre_release_review',
    'Aggregator':                'aggregator',
    'Count_HUC12':               'count_huc12s',
    'Count_ElmID':               'count_elm_ids'
})
f = convertnumbers(f)
f = convert(f, (
    'id',
    'comment_id',
    'count_huc12s',
    'count_elm_ids',
), lambda v: int(v))
todb(f, connection, 'sources')

# HabitatUsage: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS habitat_usages CASCADE;
CREATE TABLE habitat_usages (
    id                INTEGER NOT NULL UNIQUE PRIMARY KEY,
    name              VARCHAR UNIQUE
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'HabitatUsage.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'HabU_ID':                  'id',
    'HabU_Name':                'name',
})
f = convertnumbers(f)
todb(f, connection, 'habitat_usages')

# Element: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS elements CASCADE;
CREATE TABLE elements (
    id                          INTEGER NOT NULL UNIQUE PRIMARY KEY,
    scientific_name             VARCHAR,
    common_name                 VARCHAR,
    taxonomic_group             VARCHAR NOT NULL,
    fwa_v1                      INTEGER,
    tax_list                    VARCHAR,
    g_rank                      VARCHAR,
    s_rank                      VARCHAR,
    elm_scin_1                  VARCHAR,
    elm_scin_2                  VARCHAR,
    elm_scin_3                  VARCHAR,
    elm_scin_4                  VARCHAR,
    kingdom                     VARCHAR,
    phylum                      VARCHAR,
    tax_class                   VARCHAR,
    tax_order                   VARCHAR,
    family                      VARCHAR,
    genus                       VARCHAR,
    species                     VARCHAR,
    subsp_var                   VARCHAR,
    kingdom_id                  VARCHAR,
    phylum_id                   VARCHAR,
    tax_class_i                 VARCHAR,
    tax_order_i                 VARCHAR,
    family_id                   VARCHAR,
    genus_id                    VARCHAR,
    species_id                  VARCHAR,
    other_id                    VARCHAR,
    sensitive_fam               VARCHAR,
    ns_endemic                  INTEGER,
    safit_endemic               INTEGER,
    other_endemic               INTEGER,
    endemism_comment            TEXT,
    fed_list                    VARCHAR,
    state_list                  VARCHAR,
    other_list                  VARCHAR,
    mgtag_list                  VARCHAR,
    listed                      BOOLEAN,
    vulnerable                  BOOLEAN,
    endemic                     BOOLEAN,
    common                      BOOLEAN,
    not_evaluated               BOOLEAN,
    extinct                     BOOLEAN,
    status                      VARCHAR
);
CREATE INDEX ON elements (id);
CREATE INDEX ON elements (taxonomic_group);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Elements.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'ELM_SCINAM':             'scientific_name',
    'ELM_COMNAM':             'common_name',
    'GROUP_':                 'taxonomic_group',
    'FWA_v1':                 'fwa_v1',
    'TAX_LIST':               'tax_list',
    'G_Rank':                 'g_rank',
    'S_Rank':                 's_rank',
    'ELM_SCIN_1':             'elm_scin_1',
    'ELM_SCIN_2':             'elm_scin_2',
    'ELM_SCIN_3':             'elm_scin_3',
    'ELM_SCIN_4':             'elm_scin_4',
    'Kingdom':                'kingdom',
    'Phylum':                 'phylum',
    'TaxClass':               'tax_class',
    'TaxOrder':               'tax_order',
    'Family':                 'family',
    'Genus':                  'genus',
    'Species':                'species',
    'Subsp_Var':              'subsp_var',
    'Kingdom_ID':             'kingdom_id',
    'Phylum_ID':              'phylum_id',
    'TaxClass_I':             'tax_class_i',
    'TaxOrder_I':             'tax_order_i',
    'Family_ID':              'family_id',
    'Genus_ID':               'genus_id',
    'Species_ID':             'species_id',
    'ELM_ID':                 'id',
    'Other_ID':               'other_id',
    'Sensitive_Fam':          'sensitive_fam',
    'NS_endemic':             'ns_endemic',
    'SAFIT_endemic':          'safit_endemic',
    'Other_endemic':          'other_endemic',
    'Endemism_comment':       'endemism_comment',
    'Fed_list':               'fed_list',
    'State_list':             'state_list',
    'Other_list':             'other_list',
    'MgtAg_list':             'mgtag_list',
    'Listed':                 'listed',
    'Vulnerable':             'vulnerable',
    'Endemic':                'endemic',
    'Common':                 'common',
    'Not_evaluated':          'not_evaluated',
    'Extinct':                'extinct',
    'Status':                 'status',
})
# @todo resolve this hack: Deal with the mussels (multiple rows having elm_id = 81077)
f = selectnotin(f, 'scientific_name', [
    'Anodonta californiensis',
    'Anodonta dejecta',
    'Anodonta oregonensis',
])
# Attempt to pull the comma-as-thousands separator out.
f = sub(f, (
    'fwa_v1',
    'kingdom_id',
    'phylum_id',
    'tax_class_i',
    'tax_order_i',
    'family_id',
    'genus_id',
    'species_id',
    'id',
    'other_id',
), ',', '')
# Convert the new values to integers; this can handle nulls.
f = convert(f, (
    'fwa_v1',
    'id',
), lambda v: int(v))
# Don't really have to do this, but seems cleaner.
f = convert(f, (
    'listed',
    'vulnerable',
    'endemic',
    'common',
    'not_evaluated',
    'extinct',
), { 0: False, 1 : True })
todb(f, connection, 'elements')

# AU_v_elm: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS au_v_elms CASCADE;
CREATE TABLE au_v_elms (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    elm_id                      INTEGER REFERENCES elements (id),
    huc_12                      VARCHAR,
    obs_typ_id                  INTEGER REFERENCES observation_types (id),
    source_id                   INTEGER REFERENCES sources (id),
    frequency                   DOUBLE PRECISION,
    sum_amount                  DOUBLE PRECISION
);
CREATE INDEX ON au_v_elms (elm_id);
CREATE INDEX ON au_v_elms (huc_12);
CREATE INDEX ON au_v_elms (elm_id, huc_12);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'AU_v_elm_sum.csv'))
f = cutout(f, 'OID_')
f = rename(f, {
    'Elm_ID':                   'elm_id',
    'HUC_12':                   'huc_12',
    'ObsTyp_ID':                'obs_typ_id',
    'Source_ID':                'source_id',
    'FREQUENCY':                'frequency',
    'SUM_Amount':               'sum_amount',
})
f = sub(f, (
    'elm_id',
    'source_id',
    'sum_amount',
), ',', '')
f = convert(f, ('elm_id', 'source_id'), lambda v: int(float(v)))
f = convert(f, ('sum_amount'), lambda v: float(v))
todb(f, connection, 'au_v_elms')

# Persist and be tidy
connection.commit()
cursor.close()
connection.close()
