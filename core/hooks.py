import asyncio

from libqtile import hook

from core.screens import screens

bars = [screen.top for screen in screens]
margins = [sum(bar.margin) if bar else 1 for bar in bars]  # type: ignore


@hook.subscribe.startup
def startup():
    for i, bar in enumerate(bars):
        if margins[i] > 0:
            continue
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
