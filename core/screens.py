# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

wallpaper = '~/wallpapers/wp1.png'
screen_height = 768

def calculate(height: int) -> dict:
    size = height * 25 / 1080
    border = height * 6 / 1080

    return {
        'size': round(size),
        'border': round(border),
    }

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
