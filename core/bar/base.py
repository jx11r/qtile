from importlib import import_module
from os import listdir
from os.path import isfile, join

from libqtile import bar

from extras import PowerLineDecoration, RectDecoration
from utils.config import directory

defaults = {
    "font": "SauceCodePro Nerd Font Medium",
    "fontsize": 10,
    "padding": None,
}


class Bar:
    def __init__(self, theme: str) -> None:
        self.theme = theme

    @property
    def themes(self) -> set[str]:
        path = join(directory(), "core", "bar")
        excluded_files = {"__init__.py", "base.py"}
        files: list[str] = []
        for file in listdir(path):
            if isfile(join(path, file)) and file not in excluded_files:
                files.append(file.rstrip(".py"))
        return set(files)

    @property
    def config(self) -> dict | None:
        if self.theme not in self.themes:
            return None
        module = import_module(f"core.bar.{self.theme}")
        module.bar.update({"widgets": module.widgets()})
        return module.bar

    def create(self) -> bar.BarType | None:
        if self.config:
            return bar.Bar(**self.config)
        return None


def base(bg: str | None, fg: str) -> dict:
    return {
        "background": bg,
        "foreground": fg,
    }


def icon_font(size=15) -> dict:
    font = "SauceCodePro Nerd Font"
    return {"font": font, "fontsize": size}


def powerline(path: str | list[tuple], size=9) -> dict:
    return { "decorations": [
        PowerLineDecoration(
            path=path,
            size=size,
        )
    ]}  # fmt: skip


def rectangle(side: str = "") -> dict:
    return { "decorations": [
        RectDecoration(
            filled = True,
            radius = {
                "left": [8, 0, 0, 8],
                "right": [0, 8, 8, 0]
            }.get(side, 8),
            use_widget_background = True,
        )
    ]}  # fmt: skip
