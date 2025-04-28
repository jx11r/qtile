from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from extras import float_to_front
from utils.config import cfg

ctl = "control"
if cfg.is_xephyr:
    mod = "mod1"
    restart = lazy.restart()
else:
    mod = "mod4"
    restart = lazy.reload_config()

if not cfg.term["main"]:
    cfg.term["main"] = guess_terminal()

keys = [Key(*key) for key in [  # type: ignore
    # switch between windows
    ([mod], "h", lazy.layout.left()),
    ([mod], "n", lazy.layout.down()),
    ([mod], "e", lazy.layout.up()),
    ([mod], "i", lazy.layout.right()),

    # move windows between columns
    ([mod, "shift"], "h", lazy.layout.shuffle_left()),
    ([mod, "shift"], "n", lazy.layout.shuffle_down()),
    ([mod, "shift"], "e", lazy.layout.shuffle_up()),
    ([mod, "shift"], "i", lazy.layout.shuffle_right()),

    # increase/decrease window size
    ([mod], "u", lazy.layout.shrink()),
    ([mod], "y", lazy.layout.grow()),

    # window management
    ([mod, "shift"], "space", lazy.layout.flip()),
    ([mod], "m", lazy.layout.maximize()),
    ([mod], "a", lazy.window.kill()),
    ([], "F11", lazy.window.toggle_fullscreen()),

    # floating window management
    ([mod, ctl], "f", lazy.function(float_to_front)),
    ([mod], "space", lazy.window.toggle_floating()),
    ([mod], "c", lazy.window.center()),

    # toggle between layouts
    ([mod], "Tab", lazy.next_layout()),

    # qtile stuff
    ([mod, ctl], "b", lazy.hide_show_bar()),
    ([mod, ctl], "s", lazy.shutdown()),
    ([mod, ctl], "r", restart),

    # terminal
    ([mod], "Return", lazy.spawn(cfg.term["main"])),
    ([mod, "shift"], "Return", lazy.spawn(cfg.term["alt"])),

    # app launcher
    ([mod, "shift"], "r", lazy.spawn("rofi -show window")),
    ([mod], "r", lazy.spawn("rofi -show drun")),

    # web browser
    ([mod], "b", lazy.spawn(cfg.browser)),

    # file manager
    ([mod], "t", lazy.spawn(cfg.file_manager)),

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
]]  # fmt: skip
