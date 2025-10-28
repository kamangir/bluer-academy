from typing import List, Union, Dict

from bluer_objects import file


class Topic:
    def __init__(
        self,
        name: str,
        agenda: List[str],
        duration: float,
        cost: Union[float, str] = 0,
        requires: Union[str, List[str]] = "",
        items: Dict[str, str] = {},
    ):
        self.name: str = name
        self.agenda: List[str] = agenda
        self.cost: Union[float, str] = cost if isinstance(cost, str) else float(cost)
        self.duration: float = float(duration)
        self.requirements: List[str] = [
            requirement
            for requirement in (
                requires if isinstance(requires, list) else requires.split(",")
            )
            if requirement
        ]
        self.required_for: List[str] = []
        self.items = items

    def filename(
        self,
        create: bool = False,
    ) -> str:
        reference = file.path(__file__)
        filename = file.absolute(
            f"../../docs/academy/syllabus/{self.name}.md",
            reference,
        )

        if not create or file.exists(filename):
            return filename

        template_filename = file.absolute(
            "../../docs/academy/syllabus/template-template.md",
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
        return (
            ["includes:"]
            + [f"- {item}." for item in self.agenda]
            + ["", "---", ""]
            + (
                [
                    "⬅️ requires: {}".format(
                        ", ".join(
                            f"[{topic_name}](./{topic_name}.md)"
                            for topic_name in self.requirements
                        )
                    ),
                ]
                if self.requirements
                else []
            )
            + [""]
            + (
                [
                    "➡️ required for: {}".format(
                        ", ".join(
                            f"[{topic_name}](./{topic_name}.md)"
                            for topic_name in self.required_for
                        )
                    ),
                ]
                if self.required_for
                else []
            )
            + (
                [
                    "",
                    f"⏳ duration: {self.duration:.1f} hours",
                ]
                if self.duration
                else []
            )
            + (
                [
                    "",
                    (
                        f"💰 cost: {self.cost:.2f} mT"
                        if isinstance(self.cost, float)
                        else f"💰 needs {self.cost}."
                    ),
                ]
                if self.cost
                else []
            )
        )
