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

    def graph(self) -> Tuple[bool, nx.DiGraph]:
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

        return True, G

    @property
    def list_of_topic_names(self) -> List[str]:
        return [topic.name for topic in self.list_of_topics]

    def test(self) -> bool:
        success, G = self.graph()

        return success
