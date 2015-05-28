## ca-freshwater-species-backend-rest-framework

### What is this?

This is the code underlying the Freshwater Species Database API. It's a fairly straightforward combination of
Django w/GeoDjango, PostgreSQL w/PostGIS, plus Django Rest Framework, its Geographic add-on, django-rest-framework-gis,
and Leaflet. The freshwater species data was collected from many source by The Nature Conservancy, and the geospatial
data by Hydrological Unit Code (HUC) is from the USGS.

### Installing your own

```
$ shp2pgsql -I -s 3310:4326 AU_CA.shp huc12s | psql -d ca_freshwater_species
$ psql ca_freshwater_species
ca_freshwater_species=# ALTER TABLE huc12s DROP CONSTRAINT huc12s_pkey;
ca_freshwater_species=# ALTER TABLE huc12s ADD PRIMARY KEY (huc_12);
```

```
-- Create a topology
SELECT CreateTopology('huc12s_topo', find_srid('public', 'huc12s', 'geom'));

-- Add a layer
SELECT AddTopoGeometryColumn('huc12s_topo', 'public', 'huc12s', 'topogeom', 'MULTIPOLYGON');

-- Populate the layer and the topology
UPDATE huc12s SET topogeom = toTopoGeom(geom, 'huc12s_topo', 1);
```

```
ca_freshwater_species=# UPDATE huc12s SET z6 = ST_SnapToGrid(ST_Simplify(topogeom, .01), 0.01);
ca_freshwater_species=# UPDATE huc12s SET z7 = z6;
ca_freshwater_species=# UPDATE huc12s SET z8 = ST_SnapToGrid(ST_Simplify(topogeom, .001), 0.001);
ca_freshwater_species=# UPDATE huc12s SET z9 = z8;
ca_freshwater_species=# UPDATE huc12s SET z10 = z8;
ca_freshwater_species=# UPDATE huc12s SET z11 = z8;
ca_freshwater_species=# UPDATE huc12s SET z12 = ST_SnapToGrid(ST_Simplify(topogeom, .0001), 0.0001);
ca_freshwater_species=# UPDATE huc12s SET z13 = z12;
ca_freshwater_species=# UPDATE huc12s SET z14 = z12;
ca_freshwater_species=# UPDATE huc12s SET z15 = z12;
```


