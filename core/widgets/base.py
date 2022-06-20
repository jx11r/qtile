# --==[ Widget Base ]==--

from libqtile import widget

font = 'SauceCodePro Nerd Font Medium'
icon_font = 'SauceCodePro Nerd Font'

defaults = {
    'font': font,
    'fontsize': 10,
    'padding': 0,
}

def base(bg: str, fg: str) -> dict:
    return {
        'background': bg,
        'foreground': fg,
    }

def spacer(bg: str) -> object:
    return widget.Spacer(background = bg)
