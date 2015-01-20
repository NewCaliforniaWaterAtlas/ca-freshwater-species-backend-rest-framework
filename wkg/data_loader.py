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
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    org_id                      INTEGER NOT NULL UNIQUE,
    org_name                    VARCHAR(32) NOT NULL
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Origin.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'Org_ID':                   'org_id',
    'Org_Name':                 'org_name',
})
f = convertnumbers(f)
todb(f, connection, 'origins')

# ObservationType: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS observation_types CASCADE;
CREATE TABLE observation_types (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    obs_typ_id                  INTEGER UNIQUE,
    obs_typ_name                VARCHAR(64) NOT NULL UNIQUE,
    range_obs                   VARCHAR(32),
    current_other               VARCHAR(32),
    group_                      VARCHAR(32)
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'ObservationType.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'ObsTyp_ID':                'obs_typ_id',
    'ObsTyp_Name':              'obs_typ_name',
    'Range_Obs':                'range_obs',
    'Current_Other':            'current_other',
    'Group_':                   'group_',
})
f = convertnumbers(f)
todb(f, connection, 'observation_types')

# Source: create, map, and load
#
# @todo source_name should be UNIQUE.
cursor.execute("""
DROP TABLE IF EXISTS sources CASCADE;
CREATE TABLE sources (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    source_id                   INTEGER NOT NULL UNIQUE,
    source_name                 VARCHAR(256),
    sourcegrp_name              VARCHAR(64),
    use_agree                   TEXT,
    permission_request_needed   VARCHAR(64),
    permission_contact_name     VARCHAR(32),
    permission_contact_email    VARCHAR(64),
    permission_status           TEXT,
    permission                  VARCHAR(32),
    comment_id                  INTEGER,
    citation                    TEXT,
    weblink                     VARCHAR(128),
    pre_release_review          VARCHAR(8),
    aggregator                  VARCHAR(32),
    count_huc12s                INTEGER,
    count_elm_ids               INTEGER
);
CREATE INDEX ON sources (source_id);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Source.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'Source_ID':                 'source_id',
    'Source_Name':               'source_name',
    'SourceGrp_Name':            'sourcegrp_name',
    'Use_agree':                 'use_agree',
    'Permission_request_needed': 'permission_request_needed',
    'Permission_contact_name':   'permission_contact_name',
    'Permission_contact_email':  'permission_contact_email',
    'Permission_status':         'permission_status',
    'Permission':                'permission',
    'Comment_ID':                'comment_id',
    'Citation':                  'citation',
    'Weblink':                   'weblink',
    'Pre_release_review':        'pre_release_review',
    'Aggregator':                'aggregator',
    'Count_HUC12s':              'count_huc12s',
    'Count_Elm_IDs':             'count_elm_ids'
})
f = convertnumbers(f)
f = convert(f, (
    'source_id',
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
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    hab_usage_id                INTEGER UNIQUE,
    hab_usage_name              VARCHAR(32) UNIQUE
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'HabitatUsage.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'HabU_ID':                  'hab_usage_id',
    'HabU_Name':                'hab_usage_name',
})
f = convertnumbers(f)
todb(f, connection, 'habitat_usages')

# Element: create, map, and load
#
cursor.execute("""
DROP TABLE IF EXISTS elements CASCADE;
CREATE TABLE elements (
    id                          BIGSERIAL NOT NULL UNIQUE PRIMARY KEY,
    elm_scinam                  VARCHAR(64),
    elm_comnam                  VARCHAR(64),
    group_                      VARCHAR(32) NOT NULL,
    fwa_v1                      INTEGER,
    tax_list                    VARCHAR(32),
    g_rank                      VARCHAR(16),
    s_rank                      VARCHAR(32),
    elm_scin_1                  VARCHAR(64),
    elm_scin_2                  VARCHAR(64),
    elm_scin_3                  VARCHAR(64),
    elm_scin_4                  VARCHAR(64),
    kingdom                     VARCHAR(32),
    phylum                      VARCHAR(32),
    tax_class                   VARCHAR(32),
    tax_order                   VARCHAR(32),
    family                      VARCHAR(32),
    genus                       VARCHAR(32),
    species                     VARCHAR(32),
    subsp_var                   VARCHAR(32),
    kingdom_id                  VARCHAR(5),
    phylum_id                   VARCHAR(5),
    tax_class_i                 VARCHAR(5),
    tax_order_i                 VARCHAR(5),
    family_id                   VARCHAR(5),
    genus_id                    VARCHAR(5),
    species_id                  VARCHAR(5),
    elm_id                      INTEGER NOT NULL UNIQUE,
    other_id                    VARCHAR(5),
    sensitive_fam               VARCHAR(32),
    ns_endemic                  INTEGER,
    safit_endemic               INTEGER,
    other_endemic               INTEGER,
    endemism_comment            TEXT,
    fed_list                    VARCHAR(64),
    state_list                  VARCHAR(64),
    other_list                  VARCHAR(64),
    mgtag_list                  VARCHAR(32),
    listed                      BOOLEAN,
    vulnerable                  BOOLEAN,
    endemic                     BOOLEAN,
    common                      BOOLEAN,
    not_evaluated               BOOLEAN,
    extinct                     BOOLEAN,
    status                      VARCHAR(32)
);
CREATE INDEX ON elements (elm_id);
CREATE INDEX ON elements (group_);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'Elements.csv'))
f = cutout(f, 'OBJECTID')
f = rename(f, {
    'ELM_SCINAM':             'elm_scinam',
    'ELM_COMNAM':             'elm_comnam',
    'GROUP_':                 'group_',
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
    'ELM_ID':                 'elm_id',
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
f = selectnotin(f, 'elm_scinam', [
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
    'elm_id',
    'other_id',
), ',', '')
# Convert the new values to integers; this can handle nulls.
f = convert(f, (
    'fwa_v1',
    'elm_id',
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
    elm_id                      INTEGER REFERENCES elements (elm_id),
    huc_12                      VARCHAR(12),
    obs_typ_id                  INTEGER REFERENCES observation_types (obs_typ_id),
    source_id                   INTEGER REFERENCES sources (source_id),
    frequency                   DOUBLE PRECISION,
    sum_amount                  DOUBLE PRECISION
);
""")
f = fromcsv(os.path.join('wkg', args.subdir, 'AU_v_Elm_sum.csv'))
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
