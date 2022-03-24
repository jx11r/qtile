# --==[ Qtile Bar ]==--

from .widgets import *

# Layouts
widgets = [
    padding(),
    *logo(color[16], color[12]),
    sep(color[16]),

    *cpu(color[16], color[5], color[5]),
    sep('#'),
    *ram(color[16], color[3], color[3]),

    sep(color[16]),
    *spotify(color[16], color[2], color[2]),

    spacer(None),
    *groups(None),
    spacer(None),

    *volume(color[16], color[2], color[2]),

    sep(color[16]),
    *weather(color[16], color[3], color[3]),

    sep(color[16]),
    *clock(color[16], color[4], color[4]),
    padding(),
]
