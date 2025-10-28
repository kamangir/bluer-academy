from bluer_objects.README.consts import assets_url

from bluer_academy.academy.classes.topic import Topic
from bluer_academy.academy.syllabus.consts import (
    bluer_ugv_blob,
    bluer_ugv_root,
    bluer_ugv_tree,
)

topic = Topic(
    "ugv",
    [
        "unmanned ground vehicles: basics",
        f"[ugv computer design]({bluer_ugv_blob}/docs/swallow/digital/design)",
        f"related technologies: power management, motor drivers, pwm, [ultrasonic sensors]({bluer_ugv_blob}/docs/swallow/digital/design/ultrasonic-sensor), [ble](https://github.com/kamangir/bluer-algo/blob/main/bluer_algo/docs/bps)",
        f"[PCB prototyping]({bluer_ugv_tree}/docs/swallow/digital/design/shield.md)",
    ],
    duration=12,
    requires="sbc,machine-vision",
    items={
        assets_url(suffix="arzhang/VID-20250905-WA0014_1.gif"): bluer_ugv_root,
    },
)
