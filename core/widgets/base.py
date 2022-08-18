from libqtile import widget
from extras import PowerLineDecoration, RectDecoration

# This font mustn't be modified.
icon_font = 'SauceCodePro Nerd Font'

defaults = dict(
  font = 'SauceCodePro Nerd Font Medium',
  fontsize = 10,
  padding = None,
)

def base(bg: str, fg: str) -> dict:
  return {
    'background': bg,
    'foreground': fg,
  }

def decoration(side: str = 'both') -> dict:
  radius = {'left': [8, 0, 0, 8], 'right': [0, 8, 8, 0]}
  return { 'decorations': [
    RectDecoration(
      filled = True,
      radius = radius.get(side, 8),
      use_widget_background = True,
    )
  ]}

def font(fontsize: int) -> dict:
  return {
    'font': icon_font,
    'fontsize': fontsize,
  }

def icon(bg: str, fg: str) -> dict:
  return {
    **base(bg, fg),
    **font(15),
  }

def powerline(path: str | list, size: int = 9) -> dict:
  return { 'decorations': [
    PowerLineDecoration(
      path = path,
      size = size,
    )
  ]}

def spacer(bg: str) -> object:
  return widget.Spacer(background = bg)
