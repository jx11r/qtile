from libqtile.config import Group, Key
from libqtile.lazy import lazy

from core import bar
from core.keys import keys, mod
from utils.match import wm_class

groups, tag = [], bar.tags

for i, (key, layout, matches) in enumerate([
    ("1", None, wm_class(["wezterm"])),
    ("2", "max", wm_class(["code"])),
    ("3", None, wm_class(["insomnia", "obs", "evince"])),
    ("q", "max", wm_class(["brave-browser", "firefox"])),
    ("w", "max", wm_class(["discord", "telegram-desktop"])),
    ("e", "max", wm_class(["spotify", "vlc"])),
]):  # fmt: skip
    groups.append(Group(key, matches, layout=layout, label=tag[i]))

for group in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], group.name, lazy.group[group.name].toscreen(toggle=True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], group.name, lazy.window.togroup(group.name)),
    ])  # fmt: skip
