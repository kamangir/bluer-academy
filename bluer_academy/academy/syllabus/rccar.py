from bluer_objects.README.consts import assets_url


from bluer_academy.academy.classes.topic import Topic
from bluer_academy.academy.syllabus.consts import bluer_ugv_tree, bluer_ugv_blob

topic = Topic(
    "rccar",
    [
        f"[basic remote control car]({bluer_ugv_tree}/docs/ravin/ravin3)",
        f"[Arduino control car]({bluer_ugv_tree}/docs/ravin/ravin4) 🚧",
    ],
    duration=6,
    requires="documentation,basic-electronics",
    items={
        "{}/20250723_095155~2_1.gif".format(
            assets_url(
                suffix="ravin",
                volume=2,
            )
        ): f"{bluer_ugv_blob}/docs/ravin/ravin3",
        "{}/20251014_164022.jpg".format(
            assets_url(
                suffix="ravin4",
                volume=2,
            )
        ): f"{bluer_ugv_blob}/docs/ravin/ravin4",
    },
)
