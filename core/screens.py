# --==[ Screens ]==--

from libqtile import bar
from libqtile.config import Screen

import core.widgets as widgets

BAR = bar.Bar(**widgets.bar)

config = {
  'wallpaper': '~/wallpapers/wp6.png',
  'wallpaper_mode': 'fill',
}

screens = [
  Screen(**config, top = BAR), # type: ignore
  Screen(**config), # type: ignore
  Screen(**config), # type: ignore
]
