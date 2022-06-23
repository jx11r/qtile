from libqtile import widget

from core.widgets.base import base, spacer
from extras import RectDecoration
from utils import color

tags: list[str] = ['●'] * 6

bar: dict = {
  'background': color[16],
  'border_color': color[16],
  'border_width': 4,
  'margin': [10, 10, 0, 10],
  'opacity': 1,
  'size': 18,
}

widgets: list = [
  widget.Spacer(length = 15),
  widget.TextBox('lol'),
]
