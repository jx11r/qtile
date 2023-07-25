import json
import os
from dataclasses import asdict, dataclass
from os import path


@dataclass
class Config:
    bar: str = "shapes"
    bar2: str = ""
    browser: str = ""
    term: str | None = ""
    term2: str = ""
    wallpaper: str = ""


def directory():
    xdg = path.expanduser("~/.config/qtile")
    return xdg if path.exists(xdg) else os.getcwd()


file = path.join(directory(), "cfg.json")

if not path.exists(file):
    cfg = Config()
    with open(file, "w") as f:
        content = asdict(cfg)
        f.write(json.dumps(content, indent=2))
else:
    with open(file, "r") as f:
        content = json.load(f)
        cfg = Config(**content)
