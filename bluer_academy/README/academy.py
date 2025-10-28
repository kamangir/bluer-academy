from bluer_academy.academy.syllabus import syllabus


docs = [
    {
        "path": "../docs/academy",
        "macros": {
            "table:::": syllabus.as_markdown[1],
            "duration:::": [
                f"⏳ duration: {syllabus.duration} hours",
            ],
        },
    },
] + [
    {
        "path": topic.filename(create=True),
        "items": topic.items,
        "macros": {
            "content:::": topic.as_markdown,
        },
    }
    for topic in syllabus.list_of_topics
]
