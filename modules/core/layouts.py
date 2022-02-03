# --==[ Layouts ]==--

from libqtile import layout
from libqtile.config import Match

from ..utils.colors import color

# Layout config
def config(layout_name):
    default = {
        'border_normal': color[8],
        'border_focus': color[5],
        'border_width': 1,
        'single_border_width': 0,
        'margin': 9,
        'single_margin': 9,
    }

    if layout_name == 'bsp':
        add_config = {
            'fair': False,
            'grow_amount': 3,
            'lower_right': False,
        }
    elif layout_name == 'xmonad':
        add_config = {
            'min_ratio': 0.30,
            'max_ratio': 0.70,
            'change_ratio': 0.02,
        }
    elif layout_name == 'stack':
        add_config = {
            'border_width': 0,
            'num_stacks': 1,
        }
    else:
        add_config = {}

    default.update(add_config)
    return default

layouts = [
    # layout.Max(),
    layout.Bsp(**config('bsp')),
    layout.MonadTall(**config('xmonad')),
    layout.MonadWide(**config('xmonad')),
    layout.Stack(**config('stack')),
]

# Floating windows
floating_layout = layout.Floating(
    float_rules = [
        *layout.Floating.default_float_rules,
        Match(wm_class = 'confirmreset'),
        Match(wm_class = 'makebranch'),
        Match(wm_class = 'maketag'),
        Match(wm_class = 'ssh-askpass'),
        Match(title = 'branchdialog'),
        Match(title = 'pinentry'),
    ],
    border_normal = color[8],
    border_focus = color[7],
    border_width = 1,
)
