from importlib import import_module

from libqtile.bar import Bar

from utils.config import cfg

themes = ["decorated"]

if cfg.bar in themes:
    module = import_module(f"core.bar.{cfg.bar}")
    module.bar.update({"widgets": module.widgets})
    bar: tuple[Bar | None, list] = (
        Bar(**module.bar),
        module.tags,
    )
else:
    bar = (None, [None] * 10)
