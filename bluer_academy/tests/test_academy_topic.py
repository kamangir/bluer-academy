from bluer_academy.academy.syllabus import math

from bluer_objects import file


def test_academy_topic():
    topic = math.topic

    assert isinstance(topic.name, str)

    assert isinstance(topic.agenda, list)
    for item in topic.agenda:
        assert isinstance(item, str)

    assert isinstance(topic.requirements, list)
    for item in topic.requirements:
        assert isinstance(item, str)

    assert isinstance(topic.as_markdown, list)
    for item in topic.as_markdown:
        assert isinstance(item, str)

    filename = topic.filename(create=True)
    assert file.exists(file.add_suffix(filename, "template"))
