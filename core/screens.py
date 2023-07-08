from libqtile.config import Screen

from core.bar import bar
from utils.config import cfg

screens = [
    Screen(
        wallpaper=cfg.wallpaper,
        wallpaper_mode="fill",
        top=bar,
    ),
    Screen(
        wallpaper=cfg.wallpaper,
        wallpaper_mode="fill",
    ),
]
