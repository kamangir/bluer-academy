from typing import List, Tuple
import networkx as nx

from bluer_objects.README.items import ImageItems

from bluer_academy.academy.classes.topic import Topic
from bluer_academy.logger import logger


class Syllabus:
    def __init__(
        self,
        list_of_topics: List[Topic] = [],
    ):
        self.list_of_topics: List[Topic] = list_of_topics

        assert self.expand_requirements()

    @property
    def as_markdown(self) -> Tuple[bool, List[str]]:
        success, sorted_list_of_topic_names = self.sorted_list_of_topic_names
        if not success:
            return success, []

        table: List[str] = [
            "| capstone project? | duration (hours) | depends on: |"
            + "".join(
                [
                    f" [{topic_name}](./{topic_name}.md) |"
                    for topic_name in sorted_list_of_topic_names
                ]
            ),
            "|" + "".join(["-|" for _ in range(len(sorted_list_of_topic_names) + 3)]),
        ] + [
            "| {} | {} | [{}](./{}.md) |".format(
                "📐" if self.topic(topic_name).items else "",
                "{:.1f}".format(self.duration_of(topic_name)),
                topic_name,
                topic_name,
            )
            + "".join(
                [
                    " {} |".format(
                        "ℹ️"
                        if topic_name_ in self.topic(topic_name).requirements
                        else ""
                    )
                    for topic_name_ in sorted_list_of_topic_names
                ]
            )
            for topic_name in sorted_list_of_topic_names
        ]

        return success, table

    def as_graph(self) -> Tuple[bool, nx.DiGraph]:
        G = nx.DiGraph()

        for topic in self.list_of_topics:
            for requirement in topic.requirements:
                if requirement not in self.list_of_topic_names:
                    logger.error(f"{topic.name} requires missing topic: {requirement}.")
                    return False, G

        for topic in self.list_of_topics:
            G.add_node(topic.name)

        for topic in self.list_of_topics:
            for requirement in topic.requirements:
                G.add_edge(topic.name, requirement)

        if not nx.is_directed_acyclic_graph(G):
            logger.error("graph has a loop")
            return False, G

        return True, G

    @property
    def duration(self) -> float:
        return sum(topic.duration for topic in self.list_of_topics)

    def duration_of(self, topic_name: str) -> float:
        return self.topic(topic_name).duration + sum(
            self.topic(topic_name_).duration
            for topic_name_ in self.topic(topic_name).requirements
        )

    def expand_requirements(self) -> bool:
        success, G = self.as_graph()
        if not success:
            return success

        success, sorted_list_of_topic_names = self.sorted_list_of_topic_names
        if not success:
            return success

        for topic_name in sorted_list_of_topic_names:
            topic = self.topic(topic_name)
            for topic_name_ in G.predecessors(topic_name):
                topic_ = self.topic(topic_name_)
                topic_.requirements = sorted(
                    list(set(topic_.requirements + topic.requirements))
                )

        return True

    @property
    def list_of_topic_names(self) -> List[str]:
        return [topic.name for topic in self.list_of_topics]

    @property
    def sorted_list_of_topic_names(self) -> Tuple[bool, List[str]]:
        success, G = self.as_graph()
        if not success:
            return success, []

        out_degree = {node: G.out_degree(node) for node in G.nodes()}

        visited: List[str] = []
        while True:
            roots = sorted(
                [
                    node
                    for node, deg in out_degree.items()
                    if deg == 0 and node not in visited
                ]
            )
            if not roots:
                break

            visited += roots

            for node in roots:
                for neighbor in sorted(G.predecessors(node)):
                    out_degree[neighbor] -= 1

        return True, visited

    def topic(self, topic_name: str) -> Topic:
        for topic in self.list_of_topics:
            if topic.name == topic_name:
                return topic

        raise NameError(f"topic: {topic_name} not found")
