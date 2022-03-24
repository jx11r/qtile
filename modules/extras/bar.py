# --==[ Qtile Bar ]==--

from .widgets import *

# Layouts
widgets = [
    padding(),
    *logo(color[0], color[12]),
    sep(color[0]),

    *cpu(color[0], color[5], color[5]),
    sep('#'),
    *ram(color[0], color[3], color[3]),

    sep(color[0]),
    *spotify(color[0], color[2], color[2]),

    spacer(None),
    *groups(None),
    spacer(None),

    *volume(color[0], color[2], color[2]),

    sep(color[0]),
    *weather(color[0], color[3], color[3]),

    sep(color[0]),
    *clock(color[0], color[4], color[4]),
    padding(),
]
