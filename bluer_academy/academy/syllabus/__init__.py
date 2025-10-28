from bluer_academy.academy.classes.syllabus import Syllabus
from bluer_academy.academy.syllabus import (
    bash,
    cloud,
    documentation,
    geospatial,
    github,
    linux,
    objects,
    math,
    plugins,
    pypi,
    python,
    testing,
)

syllabus = Syllabus(
    [
        module.topic
        for module in [
            bash,
            cloud,
            documentation,
            geospatial,
            github,
            linux,
            objects,
            math,
            plugins,
            pypi,
            python,
            testing,
        ]
    ]
)
