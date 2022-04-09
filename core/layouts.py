# --==[ Layouts ]==--

from libqtile import layout
from libqtile.config import Match

from utils.colors import color

# ---- Tiling ---------------------------- #
config = {
    'single_border_width': 0,
    'border_width': 0,
    'single_margin': 9,
    'margin': 9,
    'border_normal': '#00000000',
    'border_focus': color[5],
}

layouts = [
    layout.MonadTall(
        **config,
        min_ratio = 0.30,
        max_ratio = 0.70,
        change_ratio = 0.02,
    ),

    layout.Stack(
        **config,
        num_stacks = 1,
        # border_width = 0,
    ),
]

# ---- Floating -------------------------- #
floating_layout = layout.Floating(
    fullscreen_border_width = 0,
    border_width = 0,
    border_normal = '#00000000',
    border_focus = color[7],
    
    float_rules = [
        *layout.Floating.default_float_rules,
        Match(wm_class = [
            'confirmreset',
            'makebranch',
            'maketag',
            'ssh-askpass',
            'gnome-screenshot',
            'Xephyr',
            'lxappearance',
            'xfce4-about',
            'thunar',
        ]),

        Match(title = [
            'File Operation Progress',
            'Open File',
            'branchdialog',
            'pinentry',
        ]),
    ],
)
