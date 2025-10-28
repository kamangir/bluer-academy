from bluer_academy.academy.classes.syllabus import Syllabus
from bluer_academy.academy.syllabus import (
    bash,
    cloud,
    documentation,
    geospatial,
    geospatial_sources,
    geospatial_timeseries,
    github,
    linux,
    math,
    objects,
    plugins,
    pypi,
    python,
    QGIS,
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
            geospatial_sources,
            geospatial_timeseries,
            github,
            linux,
            objects,
            math,
            plugins,
            pypi,
            python,
            QGIS,
            testing,
        ]
    ]
)
