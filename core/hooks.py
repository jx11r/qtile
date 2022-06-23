# --==[ Hooks ]==--

from libqtile import hook
from core.screens import BAR, widgets

MARGIN = widgets.bar['margin']
TOTAL = MARGIN if type(MARGIN) is int else sum(MARGIN)

@hook.subscribe.startup
def _():
  if TOTAL == 0:
    BAR.window.window.set_property(
      'WM_NAME',
      'QTILE_BAR',
      type = 'STRING',
      format = 8,
    )
  else:
    pass
