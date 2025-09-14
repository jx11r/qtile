from libqtile.config import Group, Key
from libqtile.lazy import lazy

from core.keys import keys, mod
from utils.match import wm_class

groups: list[Group] = []

for key, label, layout, matches in [
    ("1", "", "monadtall", wm_class()),
    ("2", "", "monadtall", wm_class("code")),
    ("3", "󰆼", "monadwide", wm_class("insomnia")),
    ("4", "󰹍", "max", wm_class("obs", "gimp")),
    ("q", "󰈹", "max", wm_class("brave-browser", "firefox")),
    ("w", "󰇮", "monadtall", wm_class("discord", "Telegram")),
    ("f", "󰝰", "monadtall", wm_class("Evince")),
    ("p", "", "max", wm_class("cider", "vlc")),
]:
    groups.append(Group(key, matches, label=label, layout=layout))

    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], key, lazy.group[key].toscreen(toggle=True)),

        # mod1 + shift + letter of group = move focused window to group
        Key([mod, "shift"], key, lazy.window.togroup(key)),
    ])  # fmt: skip
