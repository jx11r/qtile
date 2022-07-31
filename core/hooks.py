import asyncio
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

@hook.subscribe.client_new
async def client_new(client):
  await asyncio.sleep(0.01)
  if client.name == 'Spotify':
    client.togroup('e')
