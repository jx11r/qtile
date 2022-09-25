from libqtile import hook

from core import widgets
from core.screens import bar

margin = widgets.bar['margin']
total = margin if type(margin) is int else sum(margin)

@hook.subscribe.startup
def startup():
  if total == 0:
    bar.window.window.set_property(
      name = 'WM_NAME',
      value = 'QTILE_BAR',
      type = 'STRING',
      format = 8,
    )

@hook.subscribe.client_name_updated
def client_name_updated(window):
  if window.name == 'Spotify':
    window.cmd_togroup(group_name = 'e')
