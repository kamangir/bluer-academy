from bluer_academy.academy.syllabus.consts import bluer_geo_blob, bluer_geo_root
from bluer_academy.academy.classes.topic import Topic

topic = Topic(
    "geospatial",
    [
        f"[geo images]({bluer_geo_root})",
        f"[geo vectors]({bluer_geo_root})",
        f"[stac]({bluer_geo_blob}/catalog)",
        f"[datacube]({bluer_geo_blob}/datacube)",
    ],
    duration=6,
    requires="python,bash,objects,cloud,plugins",
    items={},
)
