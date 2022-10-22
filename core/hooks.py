import asyncio
from libqtile import hook

@hook.subscribe.client_new
async def client_new(client):
  await asyncio.sleep(0.5)
  if client.name == 'Spotify':
    client.togroup('e')
