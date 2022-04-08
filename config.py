# --==[ Qtile Config ]==--

# Import modules
from core.keys import keys
from core.workspaces import groups
from core.workspaces import layouts, floating_layout
from core.screens import screens
from core.mouse import mouse

from core.extras.widgets import widget_defaults
from core.extras.widgets import extension_defaults

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
