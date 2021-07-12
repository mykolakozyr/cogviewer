import streamlit as st

import streamlit.components.v1 as components  # Import Streamlit

MAP_EMOJI_URL = "https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/285/world-map_1f5fa-fe0f.png"


# Set page title and favicon.
st.set_page_config(
    page_title="COG Viewer", 
    page_icon=MAP_EMOJI_URL,
    layout="wide"
)

# Display header.
st.markdown("<br>", unsafe_allow_html=True)
st.image(MAP_EMOJI_URL, width=80)

"""
# Cloud Optimized GeoTIFF Viewer
"""

coglink = st.text_input('Please insert the link to your COG file and press Enter', 'https://cogviewerapp.s3.eu-central-1.amazonaws.com/australia.tif')

# Render the HTML component with the main map
components.html('''
<html>
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.0.3/dist/leaflet.css"/>
    <style>
      #map {
        bottom: 0;
        left: 0;
        position: absolute;
        right: 0;
        top: 0;
      }
    </style>
  </head>
  <body>
    <div id="map"></div>
    <script src="https://unpkg.com/leaflet@1.0.3/dist/leaflet.js"></script>
    <script src="https://unpkg.com/proj4"></script>
    <script src="https://unpkg.com/georaster"></script>
    <script src="https://unpkg.com/georaster-layer-for-leaflet"></script>
    <script>
      // initalize leaflet map
      var map = L.map('map').setView([0, 0], 5);

      // defining zIndex for basemap to load after the raster file
      map.createPane('basemap');
      map.getPane('basemap').style.zIndex = 1;
      map.getPane('basemap').style.pointerEvents = 'none';

      var url_to_geotiff_file = "'''+coglink+'''";

      parseGeoraster(url_to_geotiff_file).then(georaster => {
        console.log("georaster:", georaster);

        /*
            GeoRasterLayer is an extension of GridLayer,
            which means can use GridLayer options like opacity.
            Just make sure to include the georaster option!
            http://leafletjs.com/reference-1.2.0.html#gridlayer
        */
        var layer = new GeoRasterLayer({
            attribution: "Custom Data",
            georaster: georaster,
            resolution: 128
        });
        layer.addTo(map);

      // add OpenStreetMap basemap
      L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
          attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
          pane: 'basemap'
      }).addTo(map);

        map.fitBounds(layer.getBounds());

    });

    </script>
    
    <!-- Google Analytics -->
    <script>
    (function(i,s,o,g,r,a,m){i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){
    (i[r].q=i[r].q||[]).push(arguments)},i[r].l=1*new Date();a=s.createElement(o),
    m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
    })(window,document,'script','https://www.google-analytics.com/analytics.js','ga');

    ga('create', 'G-4WX7731EL0', 'auto');
    ga('send', 'pageview');
    </script>
    <!-- End Google Analytics -->
    
  </body>
</html>

''', height=600)

"""
[![Follow](https://img.shields.io/twitter/follow/mykolakozyr?style=social)](https://www.twitter.com/mykolakozyr)
&nbsp[![Follow](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin&labelColor=blue)](https://www.linkedin.com/in/mykolakozyr/)
&nbsp[![Buy me a coffee](https://img.shields.io/badge/Buy%20me%20a%20coffee--yellow.svg?logo=buy-me-a-coffee&logoColor=orange&style=social)](https://www.buymeacoffee.com/mykolakozyr)

## Details
The implementation designed to be as simple as possible. The web map is based on [Leaflet.js](https://leafletjs.com/) with the usage of [Georaster layer for Leaflet](https://github.com/GeoTIFF/georaster-layer-for-leaflet).
The core of the code to render COG is mostly from [this example](https://github.com/GeoTIFF/georaster-layer-for-leaflet-example/blob/master/examples/load-cog-via-script-tag.html) by amazing [Daniel J. Dufour](https://twitter.com/DanielJDufour).
### QA
- ✅ COG in EPSG:3857
- ✅ COG in UTM projections
- :question: BigTIFF support - to be tested
### Known Limitations
- :warning: NULL Values returned as black
- :warning: Bands' combinations are not configurable
"""
