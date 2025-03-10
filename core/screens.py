from libqtile.config import Screen

from core.bar import Bar
from utils.config import cfg

screens = [
    Screen(
        wallpaper=cfg.wallpaper,
        wallpaper_mode="fill",
        top=Bar(cfg.bar["screen1"]).create(),
    ),
    Screen(
        wallpaper=cfg.wallpaper,
        wallpaper_mode="fill",
        top=Bar(cfg.bar["screen2"]).create(),
    ),
]
