import os

from bluer_options.help.functions import get_help
from bluer_objects import file, README

from bluer_academy import NAME, VERSION, ICON, REPO_NAME
from bluer_academy.help.functions import help_functions
from bluer_academy.README.items import items
from bluer_academy.README import academy, ai4k


def build():
    return (
        all(
            README.build(
                items=readme.get("items", []),
                path=os.path.join(file.path(__file__), readme["path"]),
                ICON=ICON,
                NAME=NAME,
                VERSION=VERSION,
                REPO_NAME=REPO_NAME,
                help_function=lambda tokens: get_help(
                    tokens,
                    help_functions,
                    mono=True,
                ),
                macros=readme.get("macros", {}),
            )
            for readme in [
                {
                    "path": "../..",
                    "items": items,
                },
                {
                    "path": "../docs",
                },
            ]
            + academy.docs
            + ai4k.docs
        )
        and academy.build()
    )
