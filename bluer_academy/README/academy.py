from bluer_objects.README.items import ImageItems
from bluer_objects import file

from bluer_academy.academy.syllabus import syllabus


docs = [
    {
        "path": "../docs/academy",
        "macros": {
            "table:::": syllabus.as_markdown[1],
            "duration:::": [
                f"⏳ total duration: {syllabus.duration:.1f} hours",
            ],
        },
    },
] + [
    {
        "path": topic.filename(create=True),
        "items": ImageItems(topic.items),
        "macros": {
            "content:::": topic.as_markdown,
        },
    }
    for topic in syllabus.list_of_topics
]


def build() -> bool:
    return syllabus.as_image(
        file.absolute(
            "../assets/syllabus.png",
            file.path(__file__),
        ),
    )
