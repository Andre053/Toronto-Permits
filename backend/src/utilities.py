import geopandas as gp # working with geospatial data
import geojson
import pandas as pd
import ijson
import json
from pyproj import transformer


"""
"type": "FeatureCollection",
"name": "toronto_fsa_codes_generated",
"crs": { 
    "type": "name", 
    "properties": { 
            "name": "urn:ogc:def:crs:EPSG::3347" 
        } 
    },
"features": [
    { 
        "type": "Feature", 
        "properties": { 
                "CFSAUID": "A0A", 
                "DGUID": "2021A0011A0A", 
                "PRUID": "10", 
                "PRNAME": "Newfoundland and Labrador / Terre-Neuve-et-Labrador", 
                "LANDAREA": 4136.6221 
            }, 
        "geometry": { 
            "type": "MultiPolygon", 
            "coordinates": [ [ [ [ 8986398.602857187390327, 2027249.145714320242405 ], [ 8986386.320000045001507, 2027243.745714321732521 ], [ 8986363.797142900526524, 2027253.865714319050312 ], [ 8986358.242857187986374, 2027263.151428606361151 ], [ 8986361.825714327394962, 2027274.985714320093393 ], [ 8986375.457142896950245, 2027287.334285747259855 ], [ 8986388.582857184112072, 2027289.691428605467081 ], [ 8986404.374285757541656, 2027284.902857176959515 ], [ 8986398.602857187390327, 2027249.145714320242405 ] ] ], [ [ [ 8986519.728571474552155, 2027208.137142892926931 ], [ 8986511.445714324712753, 2027202.528571464121342 ], [ 8986492.711428612470627, 2027208.454285748302937 ], [ 8986463.162857182323933, 2027258.982857178896666 ], [ 8986458.811428613960743, 2027272.202857177704573 ], [ 8986466.137142896652222, 2027298.880000036209822 ], [ 8986475.811428613960743, 2027312.420000035315752 ], [ 8986497.771428614854813, 2027331.360000032931566 ], [ 8986517.14000004529953, 2027338.417142890393734 ], [ 8986590.000000044703484, 2027333.825714319944382 ], [ 8986597.894285753369331, 2027331.431428607553244 ], [ 8986599.351428613066673, 2027320.348571464419365 ], [ 8986566.420000039041042, 2027281.92285717651248 ],

            
Old code

for element in parser:
            print(element)
            if count%50 == 0: 
                print("Parsed:", count) # track the time

            json_obj = json.loads(element)
            print(json_obj)
            fsv = json_obj["properties"]["CFSAUID"]
            if fsv in fsv_codes:
                to_keep.append(json_obj)
            count += 1

            

##### TROUBLESHOOTING

The geography data is far different in the Statcan, in the 1000s

The geography data in neighbourhoods is lat/lon

Must first transform from EPSG 3347 to EPSG 4326 (latter is the common format)
"""

JSON_BASE = {
    "type": "FeatureCollection",
    "name": "toronto_fsa_codes_generated",
    "crs": { 
        "type": "name", 
        "properties": { 
                "name": "urn:ogc:def:crs:EPSG::3347" 
            } 
        },
    "features": []
}
# ['M7A', 'M5X'] not found
FSV_CODES = "'M4V' 'M4S' 'M4C' 'M8Y' 'M8W' 'M1H' 'M6S' 'M6E' 'M2M' 'M3C' 'M4T' 'M1L' 'M6G' 'M6H' 'M6A' 'M6B' 'M5R' 'M4K' 'M5T' 'M4G' 'M1S' 'M3A' 'M1N' 'M9C' 'M6J' 'M6K' 'M4L' 'M5S' 'M6M' 'M4E' 'M8V' 'M5A' 'M6N' 'M5N' 'M9A' 'M6R' 'M4B' 'M4J' 'M3H' 'M9M' 'M9R' 'M4N' 'M2K' 'M9N' 'M3L' 'M4A' 'M1B' 'M9W' 'M6C' 'M8Z' 'M5P' 'M5M' 'M4R' 'M2J' 'M2N' 'M4W' 'M1C' 'M4M' 'M6P' 'M1M' 'M1K' 'M3B' 'M9L' 'M1E' 'M2R' 'M1R' 'M2H' 'M4X' 'M9B' 'M1X' 'M5V' 'M4P' 'M6L' 'M2P' 'M2L' 'M8X' 'M5H' 'M1P' 'M9V' 'M5B' 'M1J' 'M9P' 'M3M' 'M3K' 'M1T' 'M1V' 'M3N' 'M3J' 'M1G' 'M1W' 'M4H' 'M4Y' 'M5C' 'M5J' 'M5E' 'M5G' 'M7A' 'M5X'".replace("'", "").split(" ")


# convert to the correct GeoJSON, needs to be compliant with Leaflet system
# this requires re-projecting (https://geopandas.org/en/stable/docs/user_guide/projections.html)
def convert_shapefile(path):
    shape_file = gp.read_file(path)
    print("CRS data:", shape_file.crs)
    input("Convert to GeoJSON?")

    shape_file = shape_file.to_crs("EPSG:4326")
    print("CRS data is now:", shape_file.crs)
    input("Complete the change?")
    shape_file.to_file("../GeoData/canada_fsa_codes_cbf.geojson", driver='GeoJSON')

# only want those FSA codes within Toronto

def get_postal_codes(): 
    path = "cleared_permits_data.csv"
    df = pd.read_csv(path)
    return df["POSTAL"].unique()

def filter_geojson(path):
    data = JSON_BASE

    with open(path, "r") as f:
        features = ijson.items(f, "features.item") # parse all features
        print("Parser ready with features")
        
        keep = [feat for feat in features if feat['properties']['CFSAUID'] in FSV_CODES]
        data["features"] = keep

    #gj_features = [Feature(geometry=x["geometry"], properties=x[]) for x in data["features"]]
    #geojson_data = None

    with open("../GeoData/GeoJsons/tor_fsa_cbf.geojson", "w") as f:
        geojson.dump(data, f, indent=2)
    print("Dumped JSON")

    missing_fsvs = [f for f in FSV_CODES if f not in [x["properties"]["CFSAUID"] for x in data["features"]]]
    print("Missing FSVs:", missing_fsvs)

def main():
    # convert the shape file to a geojson file
    shapefile_path = "../GeoData/fsa_boundary_cbf/lfsa000b21a_e.shp"
    convert_shapefile(shapefile_path)

    # filter the geojson file for Toronto
    geojson_path = "../GeoData/canada_fsa_codes_cbf.geojson"
    filter_geojson(geojson_path)
    print("Completed main")

if __name__ == "__main__":
    main()

