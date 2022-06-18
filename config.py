# --==[ Qtile Config ]==--

# Import modules
from core import (
    floating_layout,
    groups,
    keys,
    layouts,
    mouse,
    screens,
)

# Config
dgroups_key_binder = None
dgroups_app_rules = [] # type: list
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = 'smart'
reconfigure_screens = True
auto_minimize = False
wmname = 'qtile'
