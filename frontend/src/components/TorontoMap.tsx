// using react-leaflet

import { MapContainer, TileLayer, GeoJSON } from 'react-leaflet';
import L from 'leaflet';
import {useState, useEffect } from 'react';
import axios from 'axios';
import './TorontoMap.css'
import List from "./List"
import TextField from "@mui/material/TextField"; // install @mui/material

/*
Sources
- https://leafletjs.com/reference.html

- React Leaflet allows us to access the open maps map of the World
- Now we need to add our FSV data relevant to this project

MapContainer
- Responsible for creating the Leaflet Map instance and providing it to its child components
- Uses a React Context

Child components
- Have their own props as options 

GeoJSON 
- Use 'L.geoJSON(<object> geojson?, <GeoJSON options> options?' to create a GeoJSON layer
- A Layer that can be added to the map
- Options
  - onEachFeature: Can be called once for each created Feature
    - Useful for attaching events and popups to features



# KEY IDEA
- Allow the neighbourhood layer to be shown for ease of use
- Allow for a search, finding the FSA from the address

# Troubleshooting
- This geo file is using urn:ogc:def:crs:EPSG::3347
  - Statistics Canada Lambert, projected coordinate system (NAD837)
- Took out the following mui TextField for search

<TextField
  id="outlined-basic"
  variant="outlined"
  fullWidth
  label="Search"
/>
*/

interface FSAStats {
    population: number
    income: number
    //[key: string]: any // why need a key?
}

const TorontoMap = () => {
    const [geoData, setGeoData] = useState<any | null>(null);
    const [selectedFSA, setSelectedFSA] = useState<string | null>(null)
    const [stats, setStats] = useState<FSAStats | null>(null)

    // the Toronto map use will get the geo data for the map
    // sets geoData to that of the geoJson file
    useEffect(() => {
        console.log("Toronto map effect called")
        fetch('/toronto_fsa_cbf.geojson') // 8 MBs of data
            .then(res => res.json())
            .then(
              data => {
                setGeoData(data)
                console.log("Data:", data)
              }
            ); // geoData is what is used
        
    }, []);

    // part of the GeoJSON object, will be called on each feature created 
    const onEachFeature = (feature: any, layer: L.Layer) => {

        // 1. get the fsa value
        //console.log("FSA", fsa) // this works on reset

        // 2. on this particular layer, this on-click event
        layer.on({
            click: () => {
                const fsa = feature.properties.CFSAUID
                setSelectedFSA(fsa);
                
                axios.get(`http://localhost:8000/stats/${fsa}`).then((res) => {
                    setStats(res.data);
                }).catch(
                    () => { 
                        console.log("Error caught")
                        setStats(null)}
                    )
                
            }
        });
        //layer.bindTooltip(feature.properties.FSA, { permanent: false });
    };

    return (
        <div style={{ display: 'flex', height: '100vh' }}>
          <MapContainer center={[43.7, -79.4]} zoom={11} style={{ height: '100%', width: '70%' }}>
            <TileLayer
              attribution='&copy; OpenStreetMap contributors'
              url="https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png"
            />
            {/*Need geoData to be set before adding the layers */}
            {geoData && (<GeoJSON data={geoData} onEachFeature={onEachFeature} style={{
                color: '#ff00ddff',
                weight: 2,
                fillOpacity: 0.5,
              }}
            />)}
            
        </MapContainer>

        {/* Sidebar for stats */}
        <div style={{ padding: '1rem', width: '30%', overflowY: 'auto', backgroundColor: '#f4f4f4' }}>
          <h1>TODO</h1>
          <p>Implement the router: Redirect for: / and /home</p>
          <p>Navbar to show various options: map, stats page, etc.</p>
          <p>Backend should have a database to continually update, see how to only get new data</p>
          <p>Improve UI, UX, and accessibility</p>
          <h1>Search</h1>
          <p>Find a specific address</p>
          <h1>React Search</h1>
          <div className="search">
            Search! (textbox here, followed by list of options?)
          </div>
          <List />
          <h1>Timeframe</h1>
          <div className="slidecontainer">
            <input type="range" min="1" max="100" value="50" className="slider" id="myRange"/>
          </div>
          <p>Range slider over the timeline from the data https://www.w3schools.com/howto/howto_js_rangeslider.asp</p>
          <h1>Map options</h1>
          <p>Show/remove different layers: FSAs, neighbourhoods (FSAs will always be used)</p>
          
          <h1>Statistics</h1>
          {selectedFSA ? (
            stats ? (
              <div>
                <h2>FSA: {selectedFSA}</h2>
                <ul>

                  {
                    // loop through kv pairs of an object
                    // throughing object error, if value is an obj, will occur
                    // error was Python stats were further enveloped as {"stats": ...}
                    Object.entries(stats).map(([key, val]) => (
                      <li key={key}>
                        <strong>{key}</strong>: {val}
                      </li>
                  ))}
                </ul>
              </div>
            ) : (
              <p>Loading stats for {selectedFSA}...</p>
            )
          ) : (
            <p>Click on a postal area to view stats.</p>
          )}
        </div>
    </div>
  );
};


export default TorontoMap
