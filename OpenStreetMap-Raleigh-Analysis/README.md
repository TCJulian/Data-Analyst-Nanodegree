# Repository for Data Wrangling Project

This projects consists of chosing a region, extracting XML data on the region from OpenStreetMap, auditing/cleaning the data in Python, converting the XML to CSV, importing the CSV into SQL, and analysing the resulting dataset using SQL queries.

The final report from the analysis can be viewed from [data_wrangling_project.md](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/data_wrangling_project.md).

## Description of Files

### docs

* [region-info.txt](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/docs/region-info.txt)
    * A brief description of the region explored and where the data was collected.
* [resources.md](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/docs/resources.md)
    * A list of any third party resources, guides, or forums posts used as references for this project.
* [sample.osm](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/docs/sample.osm)
  * A 1-10 MB sample osm from the larger osm file used in the final analysis.

### python

* [audit_phone_nums.py](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/python/audit_phone_nums.py)
    * Stores the module for auditing phone numbers when converting osm XML to CSV.
* [audit_postalcodes.py](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/python/audit_postalcodes.py)
    * Stores the module for auditing postal codes when converting osm XML to CSV.
* [audit_street_names.py](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/python/audit_street_names.py)
    * Stores the module for auditing street names when converting osm XML to CSV.
* [clean_sql.py](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/python/clean_sql.py)
    * 
* [create_sample_osm.py](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/python/create_sample_osm.py)
* [osm_to_csv.py](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/python/osm_to_csv.py)
* [schema.py](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/python/schema.py)

### sqlite

* [schema.txt](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/sqlite/schemas.txt)
* [sql_queries.md](https://github.com/TCJulian/Data-Analyst-Nanodegree/blob/master/OpenStreetMap-Raleigh-Analysis/sqlite/sql_queries.md)
