from libqtile import widget
from core.widgets.base import base, spacer

tag: list[str] = ['●'] * 6

bar = {
    'background': '#00000000',
    'border_color': '#000000',
    'border_width': 0,
    'margin': [9, 15, 0, 15],
    'opacity': 1,
    'size': 20,
}

widgets = [
    widget.GroupBox(),
]
