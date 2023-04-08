from extras import PowerLineDecoration, RectDecoration

defaults = {
    "font": "SauceCodePro Nerd Font Medium",
    "fontsize": 10,
    "padding": None,
}


def base(bg: str | None, fg: str) -> dict:
    return {
        "background": bg,
        "foreground": fg,
    }


def icon_font(size=15) -> dict:
    font = "SauceCodePro Nerd Font"
    return {"font": font, "fontsize": size}


def powerline(path: str | list, size=9) -> object:
    return PowerLineDecoration(path=path, size=size)


def rectangle(side: str = "") -> object:
    radius = {"left": [8, 0, 0, 8], "right": [0, 8, 8, 0]}
    return RectDecoration(
        filled=True,
        radius=radius.get(side.lower(), 8),
        use_widget_background=True,
    )
