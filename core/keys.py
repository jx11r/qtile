from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

browser = 'firefox'
file_manager = 'thunar'
terminal = guess_terminal()

alt = 'mod1'
mod = 'mod4'

keys = [
    # Switch between windows
    Key([mod], 'h', lazy.layout.left()),
    Key([mod], 'l', lazy.layout.right()),
    Key([mod], 'j', lazy.layout.down()),
    Key([mod], 'k', lazy.layout.up()),

    # Move windows between left, rigth, down and up
    Key([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    Key([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
    Key([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    Key([mod, 'shift'], 'k', lazy.layout.shuffle_up()),

    Key([mod], 'i', lazy.layout.grow()),                # Increase size
    Key([mod], 'm', lazy.layout.shrink()),              # Decrease size
    Key([mod], 'o', lazy.layout.maximize()),            # Maximize window
    Key([mod], 'n', lazy.layout.normalize()),           # Restore window size

    Key([mod, 'shift'], 'space', lazy.layout.flip()),   # Switch side
    Key([mod], 'f', lazy.window.toggle_fullscreen()),   # Toggle fullscreen

    Key([mod], 'c', lazy.window.center()),              # Center a floating window
    Key([mod], 'space', lazy.window.toggle_floating()), # Toggle floating

    Key([mod], 'Tab', lazy.next_layout()),              # Toggle between layouts
    Key([mod], 'a', lazy.window.kill()),                # Kill focused window
    Key([mod, 'control'], 'b', lazy.hide_show_bar()),   # Hide bar

    Key([mod, 'control'], 's', lazy.shutdown()),        # Shutdown Qtile
    Key([mod, 'control'], 'r', lazy.restart()),         # Restart Qtile
    Key([mod, alt], 'r', lazy.reload_config()),         # Reload the config
    Key([mod, alt], 's', lazy.spawn('kill -9 -1')),     # Kill Xorg session

    # Apps
    Key([mod], 'Return', lazy.spawn(terminal)),
    Key([mod], 'b', lazy.spawn(browser)),
    Key([mod], 'e', lazy.spawn(file_manager)),
 
    # Tools
    Key([mod, 'shift'], 'r', lazy.spawn('rofi -show')),
    Key([mod], 'r', lazy.spawn('rofi -show drun')),
    Key([mod], 'd', lazy.spawn('dmenu_run')),

    # Backlight
    Key([mod], 'XF86AudioLowerVolume', lazy.spawn('brightnessctl set 5%-')),
    Key([mod], 'XF86AudioRaiseVolume', lazy.spawn('brightnessctl set +5%')),

    # Volume
    Key([], 'XF86AudioMute', lazy.spawn('pamixer --togle-mute')),
    Key([], 'XF86AudioLowerVolume', lazy.spawn('pamixer --decrease 5')),
    Key([], 'XF86AudioRaiseVolume', lazy.spawn('pamixer --increase 5')),

    # Music player
    Key([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
    Key([], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
    Key([], 'XF86AudioNext', lazy.spawn('playerctl next')),
]
