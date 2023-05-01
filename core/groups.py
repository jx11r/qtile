from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from core import bar
from core.keys import keys, mod

groups, tag = [], bar.tags

for i, (key, layout, matches) in enumerate([
    ("1", None, []),
    ("2", "max", [Match(wm_class="code")]),
    ("3", None, []),
    ("q", "max", [Match(wm_class="brave-browser")]),
    ("w", "max", [Match(wm_class="discord")]),
    ("e", "max", []),
]):  # fmt: skip
    groups.append(Group(key, matches, layout=layout, label=tag[i]))  # type: ignore

for group in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], group.name, lazy.group[group.name].toscreen(toggle=True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name)),
    ])  # fmt: skip
