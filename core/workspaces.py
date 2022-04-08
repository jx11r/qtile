from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy
from libqtile import layout

from utils.settings import mod
from utils.colors import color
from core.keys import keys

# Layouts
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

# Groups
label = '●'

groups = [
    Group('1',
        label = label,
        matches = [
            Match(title = 'nvim')
        ],
    ),

    Group('2',
        label = label,
        matches = [
            Match(wm_class = 'code')
        ],
    ),

    Group('3',
        label = label,
        matches = [
            Match(wm_class = 'evince')
        ],
    ),

    Group('q',
        label = label,
        layout = 'stack',
        matches = [
            Match(wm_class = 'firefox')
        ],
    ),

    Group('w',
        label = label,
        layout = 'stack',
        matches = [
            Match(wm_class = ['telegram-desktop', 'discord']),
            Match(title = 'WhatsApp Web'),
        ],
    ),

    Group('e',
        label = label,
        layout = 'stack',
        matches = [
            Match(wm_class = ['spotify', 'vlc'])
        ],
    ),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle = True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)),
    ])
