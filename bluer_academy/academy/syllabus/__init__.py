from bluer_academy.academy.classes.syllabus import Syllabus
from bluer_academy.academy.syllabus import (
    bash,
    cloud,
    documentation,
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
        bash.topic,
        cloud.topic,
        documentation.topic,
        github.topic,
        linux.topic,
        objects.topic,
        math.topic,
        plugins.topic,
        pypi.topic,
        python.topic,
        testing.topic,
    ]
)
