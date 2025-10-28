from bluer_academy.academy.classes.topic import Topic

topic = Topic(
    "geospatial sources",
    [
        "[maxar open data](https://github.com/kamangir/bluer-geo/blob/main/bluer_geo/catalog/maxar_open_data): disaster management",
        "[copernicus](https://github.com/kamangir/bluer-geo/blob/main/bluer_geo/catalog/copernicus): sentinel2 1 & 2",
        "[firms](https://github.com/kamangir/bluer-geo/blob/main/bluer_geo/catalog/firms): fire information",
        "[global power plant](https://github.com/kamangir/bluer-geo/blob/main/bluer_geo/objects/md/global_power_plant_database.md): open source database of power plants around the world",
        "[ukraine damage map](https://github.com/kamangir/bluer-geo/blob/main/bluer_geo/catalog/ukraine_timemap)",
    ],
    duration=0,
    cost=0,
    requires="geospatial",
)
