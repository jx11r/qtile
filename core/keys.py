# --==[ Key Bindings ]==--

from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

keys, mod, alt = [], 'mod4', 'mod1'
terminal = guess_terminal()

for my_keys in [
    # Switch/move between windows
    ([mod], 'h', lazy.layout.left()),
    ([mod], 'l', lazy.layout.right()),
    ([mod], 'j', lazy.layout.down()),
    ([mod], 'k', lazy.layout.up()),

    ([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    ([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
    ([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    ([mod, 'shift'], 'k', lazy.layout.shuffle_up()),

    # Increase/decrease window size
    ([mod], 'i', lazy.layout.grow()),
    ([mod], 'm', lazy.layout.shrink()),

    # Window management
    ([mod, 'shift'], 'space', lazy.layout.flip()),
    ([mod], 'f', lazy.window.toggle_fullscreen()),
    ([mod], 'o', lazy.layout.maximize()),
    ([mod], 'n', lazy.layout.normalize()),
    ([mod], 'a', lazy.window.kill()),

    # Floating window management
    ([mod], 'space', lazy.window.toggle_floating()),
    ([mod], 'c', lazy.window.center()),

    # Toggle between layouts
    ([mod], 'Tab', lazy.next_layout()),

    # Qtile management
    ([mod, 'control'], 'b', lazy.hide_show_bar()),
    ([mod, 'control'], 's', lazy.shutdown()),
    ([mod, 'control'], 'r', lazy.reload_config()),
    ([mod, alt], 'r', lazy.restart()),

    # Kill X server
    ([mod, alt], 's', lazy.spawn('kill -9 -1')),

    # ----------- # ----------- # ----------- # ----------- #

    # Terminal
    ([mod], 'Return', lazy.spawn(terminal)),

    # Browser
    ([mod], 'b', lazy.spawn('firefox')),

    # File Manager
    ([mod], 'e', lazy.spawn('thunar')),

    # Apps Menu
    ([mod, 'shift'], 'r', lazy.spawn('rofi -show')),
    ([mod], 'r', lazy.spawn('rofi -show drun')),
    ([mod], 'd', lazy.spawn('dmenu_run')),

    # Backlight
    ([mod], 'XF86AudioLowerVolume', lazy.spawn('brightnessctl set 5%-')),
    ([mod], 'XF86AudioRaiseVolume', lazy.spawn('brightnessctl set +5%')),

    # Volume
    ([], 'XF86AudioMute', lazy.spawn('pamixer --togle-mute')),
    ([], 'XF86AudioLowerVolume', lazy.spawn('pamixer --decrease 5')),
    ([], 'XF86AudioRaiseVolume', lazy.spawn('pamixer --increase 5')),

    # Player
    ([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
    ([], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
    ([], 'XF86AudioNext', lazy.spawn('playerctl next')),
]:
    keys.append(Key(*my_keys)) # type: ignore
