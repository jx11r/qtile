from core.groups import groups
from core.keys import keys
from core.layouts import layouts, floating_layout
from core.mouse import mouse
from core.screens import screens
from core.widgets.base import defaults

widget_defaults = defaults.copy()
extension_defaults = defaults.copy()

__all__ = [
    'extension_defaults',
    'floating_layout',
    'groups',
    'keys',
    'layouts',
    'mouse',
    'screens',
    'widget_defaults',
]
