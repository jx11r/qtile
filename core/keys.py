from libqtile.config import Key
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

# Apps
browser = 'firefox'
file_manager = 'thunar'
terminal = guess_terminal()

alt = 'mod1'
mod = 'mod4'

# Key bindings
keys = []

for my_keys in [
    # Switch between windows
    ([mod], 'h', lazy.layout.left()),
    ([mod], 'l', lazy.layout.right()),
    ([mod], 'j', lazy.layout.down()),
    ([mod], 'k', lazy.layout.up()),

    # Move windows between left, rigth, down and up
    ([mod, 'shift'], 'h', lazy.layout.shuffle_left()),
    ([mod, 'shift'], 'l', lazy.layout.shuffle_right()),
    ([mod, 'shift'], 'j', lazy.layout.shuffle_down()),
    ([mod, 'shift'], 'k', lazy.layout.shuffle_up()),

    ([mod], 'i', lazy.layout.grow()),                # Increase size
    ([mod], 'm', lazy.layout.shrink()),              # Decrease size
    ([mod], 'o', lazy.layout.maximize()),            # Maximize window
    ([mod], 'n', lazy.layout.normalize()),           # Restore window size

    ([mod, 'shift'], 'space', lazy.layout.flip()),   # Switch side
    ([mod], 'f', lazy.window.toggle_fullscreen()),   # Toggle fullscreen

    ([mod], 'c', lazy.window.center()),              # Center a floating window
    ([mod], 'space', lazy.window.toggle_floating()), # Toggle floating

    ([mod], 'Tab', lazy.next_layout()),              # Toggle between layouts
    ([mod], 'a', lazy.window.kill()),                # Kill focused window
    ([mod, 'control'], 'b', lazy.hide_show_bar()),   # Hide bar

    ([mod, 'control'], 's', lazy.shutdown()),        # Shutdown Qtile
    ([mod, 'control'], 'r', lazy.restart()),         # Restart Qtile
    ([mod, alt], 'r', lazy.reload_config()),         # Reload the config
    ([mod, alt], 's', lazy.spawn('kill -9 -1')),     # Kill Xorg session

    # Apps
    ([mod], 'Return', lazy.spawn(terminal)),
    ([mod], 'b', lazy.spawn(browser)),
    ([mod], 'e', lazy.spawn(file_manager)),

    # Tools
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

    # Music player
    ([], 'XF86AudioPlay', lazy.spawn('playerctl play-pause')),
    ([], 'XF86AudioPrev', lazy.spawn('playerctl previous')),
    ([], 'XF86AudioNext', lazy.spawn('playerctl next')),
]: keys.append(Key(*my_keys)) # type: ignore
