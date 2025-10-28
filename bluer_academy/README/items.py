from bluer_objects import README
from bluer_objects.README.consts import assets2

items = README.Items(
    [
        {
            "name": "@academy",
            "description": "an academy for practical AI in Iran.",
            "marquee": f"{assets2}/academy/concepts/06.png?raw=true",
            "url": "./bluer_academy/docs/academy",
        },
        {
            "name": "ai4k",
            "description": "ai for kids.",
            "marquee": f"{assets2}/ai4k/20250604_154200.jpg?raw=true",
            "url": "./bluer_academy/docs/ai4k",
        },
    ]
)
