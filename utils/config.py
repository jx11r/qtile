import json
import os
from dataclasses import asdict, dataclass
from os import path


@dataclass
class Config:
    bar: str | None = "decorated"
    browser: str = ""
    term: str | None = ""
    term2: str | None = ""
    wallpaper: str = ""


def get_directory():
    XDG = path.expanduser("~/.config/qtile")
    if path.exists(XDG):
        return XDG
    return os.getcwd()


file = f"{get_directory()}/cfg.json"

if not path.exists(file):
    cfg = Config()
    with open(file, "w") as f:
        content = asdict(cfg)
        f.write(json.dumps(content, indent=2))
else:
    with open(file, "r") as f:
        content = json.load(f)
        cfg = Config(**content)
