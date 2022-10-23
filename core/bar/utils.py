from libqtile import widget
from extras import PowerLineDecoration, RectDecoration

defaults = {
  'font': 'SauceCodePro Nerd Font Medium',
  'fontsize': 10,
  'padding': None,
}

def base(bg: str, fg: str) -> dict:
  return {
    'background': bg,
    'foreground': fg,
  }

def decoration(side: str = '') -> dict:
  return { 'decorations': [
    RectDecoration(
      filled = True,
      radius = {
        'left': [8, 0, 0, 8],
        'right': [0, 8, 8, 0]
      }.get(side, 8),
      use_widget_background = True,
    )
  ]}

def iconFont(size = 15) -> dict:
  return {
    'font': 'SauceCodePro Nerd Font',
    'fontsize': size
  }

def powerline(path: str | list, size = 9) -> dict:
  return { 'decorations': [
    PowerLineDecoration(
      path = path,
      size = size,
    )
  ]}
