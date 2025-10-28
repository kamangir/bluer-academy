from bluer_objects.README.items import Items, ImageItems
from bluer_objects import file

from bluer_academy.academy.syllabus import syllabus


docs = [
    {
        "path": "../docs/academy",
        "items": Items(
            [
                {
                    "name": topic.name,
                    "image": list(topic.items.keys())[0],
                    "url": "./syllabus/{}.md".format(topic.name),
                }
                for topic in syllabus.list_of_topics
                if topic.items
            ]
        ),
        "cols": 5,
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
        "cols": topic.cols,
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
