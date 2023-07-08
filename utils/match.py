from libqtile.config import Match


class Matches:
    def __init__(self, property: str, values: list) -> None:
        self.property = property
        self.values = values

    def generate(self) -> list[Match]:
        return [Match(**{self.property: i}) for i in self.values]


def wm_class(values: list):
    return Matches("wm_class", values).generate()


def title(values: list):
    return Matches("title", values).generate()
