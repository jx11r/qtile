from importlib import import_module
from os import listdir
from os.path import isfile, join

from libqtile import bar

from extras import PowerLineDecoration, RectDecoration
from utils.config import cfg

defaults = {
    "font": "Hasklug Nerd Font Mono Medium",
    "fontsize": 11,
    "padding": None,
}


class Bar:
    def __init__(self, theme: str):
        self.theme = theme

    @property
    def themes(self) -> set[str]:
        path = join(cfg.path(), "core", "bar")
        excluded_files = {"__init__.py", "base.py"}
        return {
            file.removesuffix(".py")
            for file in listdir(path)
            if isfile(join(path, file)) and file not in excluded_files
        }

    @property
    def config(self) -> dict | None:
        if self.theme not in self.themes:
            return None
        module = import_module(f"core.bar.{self.theme}")
        return {"widgets": module.widgets(), **module.bar}

    def create(self) -> bar.BarType | None:
        if not self.config:
            return None
        return bar.Bar(**self.config)


def base(bg: str | None, fg: str) -> dict:
    return {
        "background": bg,
        "foreground": fg,
    }


def symbol(size=16) -> dict:
    font = "Symbols Nerd Font Mono Regular"
    return {"font": font, "fontsize": size}


def powerline(path: str | list[tuple], size=10):
    return { "decorations": [
        PowerLineDecoration(
            path=path,
            size=size,
        )
    ]}  # fmt: skip


def rectangle(side=""):
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
