# --==[ Groups ]==--

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from core.keys import keys, mod

# Icons & Tags
circles = ['●'] * 6
groups, tag = [], circles.copy()

# Workspaces
for g in (
    ('1', tag[0], '', []),
    ('2', tag[1], '', [Match(wm_class = 'code')]),
    ('3', tag[2], '', []),
    ('q', tag[3], 'stack', [Match(wm_class = 'firefox')]),
    ('w', tag[4], 'stack', [Match(wm_class = 'discord')]),
    ('e', tag[5], 'stack', [Match(wm_class = 'spotify')]),
):
    args = {'label': g[1], 'layout': g[2], 'matches': g[3]}
    groups.append(Group(name = g[0], **args)) # type: ignore

# Key Bindings
for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle = True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)),
    ])
