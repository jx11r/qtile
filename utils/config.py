import json
from dataclasses import asdict, dataclass, field
from os import environ, getcwd
from os.path import exists, expanduser, join


@dataclass
class Config:
    browser: str = "brave"
    wallpaper: str = ""
    bar: dict = field(default_factory=lambda: {"screen1": "shapes", "screen2": ""})
    term: dict = field(default_factory=lambda: {"main": "", "alt": ""})

    @property
    def is_xephyr(self):
        return int(environ.get("QTILE_XEPHYR", 0)) > 0

    @staticmethod
    def path() -> str:
        xdg = expanduser("~/.config/qtile")
        return xdg if exists(xdg) else getcwd()

    @classmethod
    def load(cls) -> "Config":
        file = join(cls.path(), "cfg.json")
        if not exists(file):
            cls.generate(file)
            return cls()
        with open(file) as f:
            content = json.load(f)
            return cls(**content)

    @classmethod
    def generate(cls, file: str):
        with open(file, "w") as f:
            content = asdict(cls())
            f.write(json.dumps(content, indent=2))


cfg = Config.load()
