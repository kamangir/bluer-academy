from typing import List, Union


class Topic:
    def __init__(
        self,
        name: str,
        items: List[str] = [],
        requires: Union[str, List[str]] = "",
    ):
        self.name = name
        self.items = items
        self.requirements = [
            requirement
            for requirement in (
                requires if isinstance(requires, list) else requires.split(",")
            )
            if requirement
        ]
