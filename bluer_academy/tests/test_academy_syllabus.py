import pytest
import networkx as nx

from bluer_academy.academy.syllabus import syllabus


def test_academy_syllabus():
    success, G = syllabus.as_graph()
    assert success
    assert isinstance(G, nx.DiGraph)

    list_of_topic_names = syllabus.list_of_topic_names
    assert isinstance(list_of_topic_names, list)
    for topic in syllabus.list_of_topic_names:
        assert isinstance(topic, str)

    success, list_of_topic_names = syllabus.sorted_list_of_topic_names
    assert success
    assert isinstance(list_of_topic_names, list)
    for topic in list_of_topic_names:
        assert isinstance(topic, str)

    topic = syllabus.topic("linux")
    assert topic.name == "linux"

    with pytest.raises(NameError):
        syllabus.topic("astronomy")

    assert isinstance(syllabus.duration, float)

    success, table = syllabus.as_markdown
    assert success
    for line in table:
        assert isinstance(line, str)

    syllabus.expand_requirements()

    duration = syllabus.duration_of("geospatial")
    assert isinstance(duration, float)
    assert duration > 0.0
