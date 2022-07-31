from libqtile.bar import Bar
from libqtile.config import Screen

from core import widgets
from utils import config

bar = Bar(**widgets.bar)

screens = [
  Screen(
    wallpaper = config['wallpaper'],
    wallpaper_mode = 'fill',
    top = bar,
  ),

  Screen(
    wallpaper = config['wallpaper'],
    wallpaper_mode = 'fill',
    # top = Bar()
  ),
]
