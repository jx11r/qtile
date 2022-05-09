# --==[ Widget Base ]==--

from libqtile import widget

font = 'SauceCodePro Nerd Font Medium'
icon_font = 'SauceCodePro Nerd Font'

widget_defaults = {
    'font': font,
    'fontsize': 10,
    'padding': 0,
}

extension_defaults = widget_defaults.copy()

def base(bg: str, fg: str) -> dict:
    return {
        'background': bg,
        'foreground': fg,
    }

def spacer(bg: str) -> object:
    return widget.Spacer(background = bg)
