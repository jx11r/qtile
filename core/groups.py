# --==[ Groups ]==--

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from .keys import keys, mod

# Icons & Tags
label = '●'

# Workspaces
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
