import asyncio

from libqtile import hook

from core.bar import bar

margin = sum(bar.margin) if bar else -1


@hook.subscribe.startup
def startup():
    if margin == 0:
        bar.window.window.set_property(
            name="WM_NAME",
            value="QTILE_BAR",
            type="STRING",
            format=8,
        )


@hook.subscribe.client_new
async def client_new(client):
    await asyncio.sleep(0.5)
    if client.name == "Spotify":
        client.togroup("e")
