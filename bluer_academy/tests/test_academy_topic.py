import networkx as nx

from bluer_academy.academy.classes.topic import Topic


def test_academy_topic():
    topic = Topic("some name")

    assert isinstance(topic.name, str)
    assert isinstance(topic.items, list)
    assert isinstance(topic.requirements, list)
