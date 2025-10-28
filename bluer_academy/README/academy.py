from bluer_objects.README.items import Items, ImageItems
from bluer_objects import file

from bluer_academy.academy.syllabus import syllabus


docs = (
    [
        {
            "path": "../docs/academy",
            "items": Items(
                [
                    {
                        "name": topic.name,
                        "marquee": list(topic.items.keys())[0],
                        "url": "./syllabus/{}.md".format(topic.name),
                    }
                    for topic in syllabus.list_of_topics
                    if topic.capstone
                ]
            ),
            "cols": 5,
            "macros": {
                "table:::": syllabus.as_markdown[1],
                "duration:::": [
                    "⏳ total duration (hours): {:.1f}".format(
                        syllabus.duration("total"),
                    ),
                    "",
                    "⏳ {} topic(s), duration (hours): {:.1f} ... {:.1f}".format(
                        len(syllabus.list_of_topics),
                        syllabus.duration("min"),
                        syllabus.duration("max"),
                    ),
                ],
            },
        },
    ]
    + [
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
    + [
        {
            "path": f"../docs/academy/instructions{doc}",
        }
        for doc in ["", "/en.md", "/fa.md"]
    ]
)


def build() -> bool:
    return syllabus.as_image(
        file.absolute(
            "../assets/syllabus.png",
            file.path(__file__),
        ),
    )
