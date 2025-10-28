from typing import List, Union

from bluer_objects import file


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

    def filename(
        self,
        create: bool = False,
    ) -> str:
        reference = file.path(__file__)
        filename = file.absolute(
            f"../../docs/academy/{self.name}.md",
            reference,
        )

        if not create or file.exists(filename):
            return filename

        template_filename = file.absolute(
            "../../docs/academy/template-template.md",
            reference,
        )
        assert file.copy(
            template_filename,
            file.add_suffix(filename, "template"),
            log=True,
        ), template_filename

        return filename

    @property
    def as_markdown(self) -> List[str]:
        return [
            "🔥",
            "",
        ] + (
            [
                "requires: {}".format(
                    ", ".join(
                        f"[{topic_name}](./{topic_name}.md)"
                        for topic_name in self.requirements
                    )
                ),
            ]
            if self.requirements
            else []
        )
