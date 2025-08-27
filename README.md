# README

## ABOUT
This project looks to analyze Toronto permit data. 

It is a full-stack program with the following architecture:

1. Frontend
The website will be implemented as a React frontend.

It will be used for displaying the information. Central will be a map and a summary statistics page. The statistics will show historical and recent stats and can be customized to show information specifically interested to the user. The map will be divided by postal codes (FSA) and show data within a time frame. This will be made using React Next.

2. Backend
The backend will use Python FastAPI.

This will query and process permit data from the database. 

3. Database
The database will be SQLite.

This will be used to store active and cleared permits.

# Tools
- Typescript, React
- Python
- SQLite

# Frontend
## The map
### Requirements
1. FSA GeoJSON Data for Toronto
Can be represented as a polygon in GeoJSON format. To obtain the information:
- Extracted from 2021 census FSA shape data

2. Map library
Leaflet is a solution. Implements Open Street Map
Open Street Map: https://wiki.openstreetmap.org/wiki/Toronto

# Things to add
Ideas for further features
## Map
- Highlight specific FSAs
- Search for a postal FSAs
- Additional map layers
- Select multiple FSAs
- Filter permits to show