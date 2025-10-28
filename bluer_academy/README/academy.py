from bluer_academy.academy.syllabus import syllabus

success, table = syllabus.as_table
assert success

docs = [
    {
        "path": "../docs/academy",
        "macros": {
            "table:::": table,
        },
    },
]
