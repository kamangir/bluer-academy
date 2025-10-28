from bluer_objects.README.consts import assets_url

from bluer_academy.academy.syllabus.consts import bluer_geo_tree, palisades_blob
from bluer_academy.academy.classes.topic import Topic

topic = Topic(
    "geospatial-timeseries",
    [
        f"[running a timeseries on Sentinel-2 on Miduk]({bluer_geo_tree}/watch)",
        f"[fire damage assessment in LA]({palisades_blob}/docs/damage-analytics.md)",
    ],
    duration=6,
    requires="geospatial,geospatial-sources,machine-vision",
    items={
        **{
            assets_url(
                suffix="{object_name}/{object_name}.gif".format(
                    object_name=object_name
                ),
            ): f"{bluer_geo_tree}/watch"
            for object_name in [
                "geo-watch-2025-05-23-2ck64x",
                "geo-watch-diff-2025-05-23-2j8p1f",
            ]
        },
        **{
            assets_url(
                suffix=f"palisades/palisades-analytics-2025-01-28-09-27-20-itglyy/{filename}"
            ): f"{palisades_blob}/docs/damage-analytics.md"
            for filename in [
                "thumbnail-039462-378510-palisades-analytics-2025-01-28-09-27-20-itglyy.gif",
                "Palisades.png",
            ]
        },
    },
    cols=2,
)
