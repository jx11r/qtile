# --==[ Workspaces ]==--

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from utils.settings import mod
from .keys import keys

label = '●'

groups = [
    Group('1', label = label),
    Group('2', label = label),
    Group('3', label = label),
    Group('q',
        label = label,
        layout = 'stack',
        matches = [Match(wm_class = 'firefox')],
    ),
    Group('w',
        label = label,
        layout = 'stack',
        matches = [Match(wm_class = 'spotify')],
    ),
    Group('e',
        label = label,
        layout = 'stack',
        matches = [Match(wm_class = ['telegram-desktop', 'discord'])],
    ),
]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle = True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)),
    ])
