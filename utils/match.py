from libqtile.config import Match


class Matches:
    def __init__(self, property: str):
        self.property = property

    def generate(self, values: tuple) -> list[Match]:
        return [Match(**{self.property: i}) for i in values]


def wm_class(*values: str):
    return Matches("wm_class").generate(values)


def title(*values: str):
    return Matches("title").generate(values)
