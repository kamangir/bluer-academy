from bluer_academy.academy.classes.topic import Topic

topic = Topic(
    "geospatial",
    [
        "[geo images](https://github.com/kamangir/bluer-geo)",
        "[geo vectors](https://github.com/kamangir/bluer-geo)",
        "[stac](https://github.com/kamangir/bluer-geo/blob/main/bluer_geo/catalog)",
        "[datacube](https://github.com/kamangir/bluer-geo/blob/main/bluer_geo/datacube)",
    ],
    duration=6,
    cost=0,
    requires="python,bash,objects,cloud,plugins",
)
