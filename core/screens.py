# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

import core.widgets as widgets

wallpaper = '~/wallpapers/wp4.png'

screens = [
    Screen(
        wallpaper = wallpaper,
        wallpaper_mode = 'fill',
        top = bar.Bar(**widgets.bar),
    ),

    Screen(
        wallpaper = wallpaper,
        wallpaper_mode = 'fill',
        # top = bar.Bar()
    ),
]
