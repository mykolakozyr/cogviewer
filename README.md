# Cloud Optimized GeoTIFF Viewer

Simple [Cloud Optimized GeoTIFF](https://www.cogeo.org/) Viewer. Just paste the COG link to the text input and press Enter.

![COG Viewer Demo](https://cogviewerapp.s3.eu-central-1.amazonaws.com/cogviewer_lite.gif)

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
