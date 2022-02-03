# --==[ Qtile Bar ]==--

from .widgets import *

# Layouts
widgets = [
    padding(),
    *logo(color[8], color[12]),
    sep(color[8]),

    *cpu(color[8], color[17], color[5]),
    sep('#'),
    *ram(color[8], color[17], color[3]),

    sep(color[8]),
    *spotify(color[8], color[17], color[2]),

    spacer(None),
    *groups(None),
    spacer(None),

    *brightness(color[8], color[17], color[1]),
    sep('#'),
    *volume(color[8], color[17], color[2]),

    sep(color[8]),
    *weather(color[8], color[17], color[3]),

    sep(color[8]),
    *clock(color[8], color[17], color[4]),
    padding(),
]
