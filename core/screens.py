# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

wallpaper = '~/wallpapers/wp1.png'

screens = [
    Screen(
        wallpaper = wallpaper,
        wallpaper_mode = 'fill',
        # top = bar.Bar(),
    ),

    Screen(
        wallpaper = wallpaper,
        wallpaper_mode = 'fill',
        # top = bar.Bar()
    ),
]
