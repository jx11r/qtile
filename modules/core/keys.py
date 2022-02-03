# --==[ Key Bindings ]==--

from libqtile.config import Key
from libqtile.lazy import lazy

from ..utils.settings import browser, file_manager
from ..utils.settings import mod, terminal

keys = [
    # Switch between windows [xmonad & bsp]
    Key([mod], 'h', lazy.layout.left()),
    Key([mod], 'l', lazy.layout.right()),
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),
    
    # Next window [xmonad]
    Key([mod], 'space', lazy.layout.next()),

    # Move windows [xmonad & bsp]
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),

    # Flip windows [bsp]
    Key([mod, 'mod1'], 'h', lazy.layout.flip_left()),
    Key([mod, 'mod1'], 'l', lazy.layout.flip_right()),
    Key([mod, 'mod1'], 'j', lazy.layout.flip_down()),
    Key([mod, 'mod1'], 'k', lazy.layout.flip_up()),

    # Flip windows [xmonad]
    Key([mod, 'shift'], 'space', lazy.layout.flip()),

    # Grow windows [bsp]
    Key([mod, 'control'], 'h', lazy.layout.grow_left()),
    Key([mod, 'control'], 'l', lazy.layout.grow_right()),
    Key([mod, 'control'], 'j', lazy.layout.grow_down()),
    Key([mod, 'control'], 'k', lazy.layout.grow_up()),

    # Grow windows [xmonad]
    Key([mod], 'i', lazy.layout.grow()),
    Key([mod], 'm', lazy.layout.shrink()),
    Key([mod], 'o', lazy.layout.maximize()),

    # Restore size [xmonad & bsp]
    Key([mod], 'n', lazy.layout.normalize()),

    # Toggle between split and unsplit sides [bsp]
    Key([mod, 'shift'], 'Return', lazy.layout.toggle_split()),

    # Toggle between layouts
    Key([mod], 'Tab', lazy.next_layout()),

    # Kill focused window
    Key([mod], 'w', lazy.window.kill()),

    # Manage Qtile
    Key([mod, 'control'], 'r', lazy.restart()),
    Key([mod, 'control'], 'q', lazy.shutdown()),
    Key([mod, 'mod1'], 'q', lazy.spawn('kill -9 -1')),

    # Terminal
    Key([mod], 'Return', lazy.spawn(terminal)),

    # Dmenu
    Key([mod], 'd', lazy.spawn('dmenu_run')),

    # Menu
    Key([mod], 'r', lazy.spawn('rofi -show drun')),
    Key([mod, 'shift'], 'r', lazy.spawn('rofi -show')),

    # Browser
    Key([mod], 'b', lazy.spawn(browser)),

    # File Manager
    Key([mod], 'e', lazy.spawn(file_manager)),
    
    # Volume
    Key([], 'XF86AudioMute', lazy.spawn('pactl set-sink-mute @DEFAULT_SINK@ toggle')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pulseaudio-ctl down +5%')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pulseaudio-ctl up +5%')),

    # Brightness
    Key([mod], 'XF86AudioLowerVolume', lazy.spawn('brightnessctl set 5%-')),
    Key([mod], 'XF86AudioRaiseVolume', lazy.spawn('brightnessctl set +5%')),

    # Player
    Key([mod], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
    Key([mod], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
    Key([mod], 'XF86AudioNext', lazy.spawn('playerctl next')),
]
