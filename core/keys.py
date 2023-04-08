from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from extras import float_to_front
from utils import config

keys, mod, alt = [], "mod4", "mod1"
terminal = config["terminal"].copy()

if not terminal["main"]:
    terminal["main"] = guess_terminal()

for key in [
    # switch between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    # move windows between columns
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "l", lazy.layout.shuffle_right()),
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),
    # increase/decrease window size
    ([mod], "i", lazy.layout.grow()),
    ([mod], "m", lazy.layout.shrink()),
    # window management
    ([mod, "shift"], "space", lazy.layout.flip()),
    ([mod], "o", lazy.layout.maximize()),
    ([mod], "n", lazy.layout.normalize()),
    ([mod], "a", lazy.window.kill()),
    ([], "F11", lazy.window.toggle_fullscreen()),
    # floating window management
    ([mod], "space", lazy.window.toggle_floating()),
    ([mod], "c", lazy.window.center()),
    ([mod], "f", lazy.function(float_to_front)),
    # toggle between layouts
    ([mod], "Tab", lazy.next_layout()),
    # qtile stuff
    ([mod, "control"], "b", lazy.hide_show_bar()),
    ([mod, "control"], "s", lazy.shutdown()),
    ([mod, "control"], "r", lazy.reload_config()),
    ([mod, alt], "r", lazy.restart()),
    # kill X11 session
    ([mod, alt], "s", lazy.spawn("kill -9 -1")),
    # terminal
    ([mod], "Return", lazy.spawn(terminal["main"])),
    ([mod, "shift"], "Return", lazy.spawn(terminal["floating"])),
    # app launcher
    ([mod, "shift"], "r", lazy.spawn("rofi -show window")),
    ([mod], "r", lazy.spawn("rofi -show drun")),
    # web browser
    ([mod], "b", lazy.spawn(config["browser"])),
    # screenshot tool
    ([], "Print", lazy.spawn("gnome-screenshot -i")),
    # backlight
    ([mod], "XF86AudioLowerVolume", lazy.spawn("brightnessctl set 5%-")),
    ([mod], "XF86AudioRaiseVolume", lazy.spawn("brightnessctl set +5%")),
    # volume
    ([], "XF86AudioMute", lazy.spawn("pamixer --toggle-mute")),
    ([], "XF86AudioLowerVolume", lazy.spawn("pamixer --decrease 5")),
    ([], "XF86AudioRaiseVolume", lazy.spawn("pamixer --increase 5")),
    # player
    ([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    ([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    ([], "XF86AudioNext", lazy.spawn("playerctl next")),
]:
    keys.append(Key(*key))  # type: ignore
