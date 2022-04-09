# --==[ Layouts ]==--

from libqtile import layout
from libqtile.config import Match

from utils.colors import color

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

floating_layout = layout.Floating(
    fullscreen_border_width = 0,
    border_width = 0,
    border_normal = '#00000000',
    border_focus = color[7],
    
    float_rules = [
        *layout.Floating.default_float_rules,
        Match(wm_class = 'confirmreset'),
        Match(wm_class = 'makebranch'),
        Match(wm_class = 'maketag'),
        Match(wm_class = 'ssh-askpass'),
        Match(wm_class = 'gnome-screenshot'),
        Match(wm_class = 'Xephyr'),
        Match(wm_class = 'lxappearance'),
        Match(wm_class = 'thunar'),
        Match(title = 'File Operation Progress'),
        Match(title = 'Open File'),
        Match(title = 'branchdialog'),
        Match(title = 'pinentry'),
    ],
)
