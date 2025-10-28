from typing import List, Tuple
import networkx as nx

from bluer_academy.academy.classes.topic import Topic
from bluer_academy.logger import logger


class Syllabus:
    def __init__(
        self,
        list_of_topics: List[Topic] = [],
    ):
        self.list_of_topics: List[Topic] = list_of_topics

    @property
    def as_table(self) -> Tuple[bool, List[str]]:
        success, sorted_list_of_topic_names = self.sorted_list_of_topic_names
        if not success:
            return False, []

        table: List[str] = [
            "".join(["| " for _ in range(len(sorted_list_of_topic_names))]) + "|",
            "".join(["|-" for _ in range(len(sorted_list_of_topic_names))]) + "|",
        ]

        return table

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
    def list_of_topic_names(self) -> List[str]:
        return [topic.name for topic in self.list_of_topics]

    @property
    def sorted_list_of_topic_names(self) -> Tuple[bool, List[str]]:
        success, G = self.as_graph()
        if not success:
            return success, []

        in_degree = {node: G.in_degree(node) for node in G.nodes()}

        roots = sorted([n for n, deg in in_degree.items() if deg == 0])

        visited = []
        stack = roots.copy()

        while stack:
            node = stack.pop(0)
            visited.append(node)

            for neighbor in sorted(G.successors(node)):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    stack.append(neighbor)
            stack.sort()

        return True, visited
