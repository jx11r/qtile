# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

from utils.settings import wallpaper
from .extras.bar import widgets

screens = [
    Screen(
        wallpaper = wallpaper,
        wallpaper_mode = 'fill',
        top = bar.Bar(
            widgets,
            size = 20,
            background = "#00000000",
            border_color = '#000000',
            border_width = 0,
            margin = [9, 15, 0, 15],
            opacity = 1,
        ),
    ),

    Screen(
        wallpaper = wallpaper,
        wallpaper_mode = 'fill',
        # top = bar.Bar()
    ),
]
