import networkx as nx

from bluer_academy.academy.syllabus import syllabus


def test_academy_syllabus():
    success, G = syllabus.graph()
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
