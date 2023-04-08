from core import hooks
from core.bar.utils import defaults
from core.groups import groups
from core.keys import keys
from core.layouts import floating_layout, layouts
from core.mouse import mouse
from core.screens import screens

widget_defaults = defaults.copy()
extension_defaults = defaults.copy()

__all__ = [
    "extension_defaults",
    "floating_layout",
    "groups",
    "hooks",
    "keys",
    "layouts",
    "mouse",
    "screens",
    "widget_defaults",
]
