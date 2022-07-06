# --==[ Hooks ]==--

import asyncio

from libqtile import hook
from core.screens import BAR, widgets

MARGIN = widgets.bar['margin']
TOTAL = MARGIN if type(MARGIN) is int else sum(MARGIN)

@hook.subscribe.startup
def startup():
  if TOTAL == 0:
    BAR.window.window.set_property(
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
