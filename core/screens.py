from libqtile.bar import Bar
from libqtile.config import Screen

from core import bar
from utils import config

screens = [
  Screen(
    wallpaper = config['wallpaper'],
    wallpaper_mode = 'fill',
    top = Bar(**bar.bar),
  ),

  Screen(
    wallpaper = config['wallpaper'],
    wallpaper_mode = 'fill',
    # top = Bar()
  ),
]
