from bluer_academy.academy.syllabus import syllabus


docs = [
    {
        "path": "../docs/academy",
        "macros": {
            "table:::": syllabus.as_table[1],
        },
    },
] + [
    {
        "path": topic.filename(create=True),
        "macros": {
            "content:::": topic.as_markdown,
            "duration:::": [f"{syllabus.cost} hours"],
        },
    }
    for topic in syllabus.list_of_topics
]
