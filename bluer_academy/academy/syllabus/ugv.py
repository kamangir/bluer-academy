from bluer_academy.academy.classes.topic import Topic

topic = Topic(
    "ugv",
    [
        "unmanned ground vehicles: basics",
        "[ugv computer design](https://github.com/kamangir/bluer-ugv/tree/main/bluer_ugv/docs/swallow/digital/design)",
        "related technologies: power management, motor drivers, pwm, [ultrasonic sensors](https://github.com/kamangir/bluer-ugv/tree/main/bluer_ugv/docs/swallow/digital/design/ultrasonic-sensor), [ble](https://github.com/kamangir/bluer-algo/blob/main/bluer_algo/docs/bps)",
        "[PCB prototyping](https://github.com/kamangir/bluer-ugv/blob/main/bluer_ugv/docs/swallow/digital/design/shield.md)",
    ],
    duration=12,
    requires="sbc,machine-vision",
)
