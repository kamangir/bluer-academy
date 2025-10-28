from bluer_academy.academy.classes.topic import Topic

topic = Topic(
    "testing",
    [
        "pylint",
        "pytest",
        "bashtest",
    ],
    duration=6,
    cost=0,
    requires="github,python,bash",
)
