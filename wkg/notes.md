query to find missing source_ids in au_v_elm that are not in the source table

select distinct a.source_id
from au_v_elms as a
left join sources as s on a.source_id = s.object_id
where s.object_id is null
order by a.source_id;

SELECT DISTINCT (huc_12, elm_id) from au_v_elms;

SELECT DISTINCT (elm_id, huc_12) from au_v_elms;

opening page stats by watershed, all species:
SELECT COUNT(DISTINCT (elm_id, huc_12)), huc_12
FROM au_v_elms
GROUP BY huc_12
ORDER BY huc_12;

taxonomic groups for menu
select count(taxonomic_group), taxonomic_group
from elements
group by taxonomic_group
order by count(taxonomic_group) desc;


Doesn't remove directories, but still
honcho run python manage.py collectstatic --clear


## Loading HUC shapefile:

```
$ shp2pgsql -I -s 3310:4326 AU_CA.shp huc12s | psql -d ca_freshwater_species
$ psql ca_freshwater_species
ca_freshwater_species=# alter table huc12s drop constraint huc12s_pkey;
ca_freshwater_species=# alter table huc12s add primary key (huc_12);
```

## Adding `SimplifyEdgeGeom`

```
CREATE OR REPLACE FUNCTION SimplifyEdgeGeom(atopo varchar, anedge int, maxtolerance float8)
RETURNS float8 AS $$
DECLARE
  tol float8;
  sql varchar;
BEGIN
  tol := maxtolerance;
  LOOP
    sql := 'SELECT topology.ST_ChangeEdgeGeom(' || quote_literal(atopo) || ', ' || anedge
      || ', ST_Simplify(geom, ' || tol || ')) FROM '
      || quote_ident(atopo) || '.edge WHERE edge_id = ' || anedge;
    BEGIN
      RAISE DEBUG 'Running %', sql;
      EXECUTE sql;
      RETURN tol;
    EXCEPTION
     WHEN OTHERS THEN
      RAISE WARNING 'Simplification of edge % with tolerance % failed: %', anedge, tol, SQLERRM;
      tol := round( (tol/2.0) * 1e16 ) / 1e16; -- round to get to zero quicker
      IF tol = 0 THEN RAISE EXCEPTION '%', SQLERRM; END IF;
    END;
  END LOOP;
END
$$ LANGUAGE 'plpgsql' STABLE STRICT;
```

In case topology is not in your `search_path`, from _outside the database of interest_
```
alter database ca_freshwater_species set search_path to "$user",public,topology;
```

If you screw up and want to resequence your topologies
```
alter sequence topology_id_seq restart;
```


Trying this for 0.1, 0.01, 0.001, 0.008, 0.0012, 0.0016, 0.0024, 0.0032, 0.0040

```
-- Create a topology
SELECT CreateTopology('huc12s_topo', find_srid('public', 'huc12s', 'geom'));

-- Add a layer
SELECT AddTopoGeometryColumn('huc12s_topo', 'public', 'huc12s', 'topogeom', 'MULTIPOLYGON');

-- Populate the layer and the topology
UPDATE huc12s SET topogeom = toTopoGeom(geom, 'huc12s_topo', 1);

-- Simplify all edges up to x degrees (original was meters, e.g., 10000 units)
SELECT SimplifyEdgeGeom('huc12s_topo', edge_id, x) FROM huc12s_topo.edge;

-- Convert the TopoGeometries to Geometries for visualization
ALTER TABLE huc12s ADD simp_x GEOMETRY;
UPDATE huc12s SET simp_x = topogeom::geometry;
```

So, looking to reduce the number of decimal places from this work; default is 15!
SELECT COUNT(gid) FROM huc12s WHERE ST_IsValid(ST_AsText(ST_SnapToGrid(simp_008, 0.001))) IS FALSE;

tolerance                                 | 0.1   | 0.01  | 0.001 | 0.008 | 0.0016 | 0.0032 | 0.0001
0.001                                     | 27    | 27    | 27    | 69    | 61     | 54     | 27
0.0001                                    | 6     | 6     | 6     | 8     | 6      | 7      | 6
0.00001                                   | 2     | 2     | 2     | 2     | 2      | 3      | 2
0.000001                                  | 2     | 2     | 2     | 2     | 2      | 2      | 2
0.0000001                                 | 0     | 0     | 0     | 0     | 0      | 0      | 0
SELECT sum(ST_NPoints(x)) FROM huc12s;    | 43455 | 42852 | 43058 | 84741 | 79661  | 77973  |

Then, with the row that produces 0:
UPDATE huc12s SET simp_x = ST_SnapToGrid(simp_x, 0.0000001);


update huc12s set simp_01 = st_astext(st_snaptogrid(st_simplify(topogeom, 0), 0.00001));

UGH

* * *

update huc12s set z6 = st_snaptogrid(st_simplify(topogeom, .01), 0.01);
update huc12s set z7 = z6;
update huc12s set z8 = st_snaptogrid(st_simplify(topogeom, .001), 0.001);
update huc12s set z9 = z8;
update huc12s set z10 = z8;
update huc12s set z11 = z8;
update huc12s set z12 = st_snaptogrid(st_simplify(topogeom, .0001), 0.0001);
update huc12s set z13 = z12;
update huc12s set z14 = z12;
update huc12s set z15 = z12;
