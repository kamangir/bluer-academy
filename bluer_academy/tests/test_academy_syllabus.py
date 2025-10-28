import networkx as nx

from bluer_academy.academy.syllabus import syllabus


def test_academy_syllabus():
    success, G = syllabus.graph()
    assert success
    assert isinstance(G, nx.DiGraph)

    assert syllabus.test()

    assert isinstance(syllabus.list_of_topic_names, list)
    for topic in syllabus.list_of_topic_names:
        assert isinstance(topic, str)
