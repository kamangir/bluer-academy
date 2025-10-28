from bluer_objects.README.consts import assets_url

from bluer_academy.academy.classes.topic import Topic

topic = Topic(
    "geospatial-timeseries",
    [
        "[running a timeseries on Sentinel-2 on Miduk](https://github.com/kamangir/bluer-geo/tree/main/bluer_geo/watch)",
    ],
    duration=6,
    requires="geospatial,geospatial-sources",
    items={
        assets_url(
            suffix="{object_name}/{object_name}.gif".format(object_name=object_name),
        ): "https://github.com/kamangir/bluer-geo/tree/main/bluer_geo/watch"
        for object_name in [
            "geo-watch-2025-05-23-2ck64x",
            "geo-watch-diff-2025-05-23-2j8p1f",
        ]
    },
)
