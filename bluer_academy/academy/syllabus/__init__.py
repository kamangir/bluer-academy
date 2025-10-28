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
    machine_vision,
    math,
    objects,
    plugins,
    pypi,
    python,
    QGIS,
    sbc,
    testing,
    ugv,
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
            machine_vision,
            objects,
            math,
            plugins,
            pypi,
            python,
            QGIS,
            sbc,
            testing,
            ugv,
        ]
    ]
)
