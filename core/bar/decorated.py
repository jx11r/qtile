from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.bar.utils import base, icon_font, powerline, rectangle
from extras import Clock, GroupBox, TextBox, Volume, modify, widget
from utils import color

bar = {
    "background": color["bg"],
    "border_color": color["bg"],
    "border_width": 4,
    "margin": [10, 10, 0, 10],
    "opacity": 1,
    "size": 18,
}

tags = ["", "", "", "󰈹", "󰇮", ""]


def sep(fg, offset=0, padding=8) -> TextBox:
    return TextBox(
        **base(None, fg),
        **icon_font(),
        offset=offset,
        padding=padding,
        text="󰇙",
    )


def logo(bg, fg) -> TextBox:
    return modify(
        TextBox,
        **base(bg, fg),
        **icon_font(),
        **rectangle(),
        mouse_callbacks={"Button1": lazy.restart()},
        offset=4,
        padding=17,
        text="",
    )


def groups(bg) -> GroupBox:
    return GroupBox(
        **icon_font(),
        background=bg,
        borderwidth=1,
        colors=[
            color["cyan"],
            color["magenta"],
            color["yellow"],
            color["red"],
            color["blue"],
            color["green"],
        ],
        highlight_color=color["bg"],
        highlight_method="line",
        inactive=color["black"],
        invert=True,
        padding=7,
        rainbow=True,
    )


def volume(bg, fg) -> list:
    return [
        modify(
            TextBox,
            **base(bg, fg),
            **icon_font(),
            **rectangle("left"),
            text="",
            x=4,
        ),
        modify(
            Volume,
            **base(bg, fg),
            **powerline("arrow_right"),
            commands={
                "decrease": "pamixer --decrease 5",
                "increase": "pamixer --increase 5",
                "get": "pamixer --get-volume-human",
                "mute": "pamixer --toggle-mute",
            },
            update_interval=0.1,
        ),
    ]


def updates(bg, fg) -> list:
    return [
        TextBox(
            **base(bg, fg),
            **icon_font(),
            offset=-1,
            text="",
            x=-5,
        ),
        widget.CheckUpdates(
            **base(bg, fg),
            **rectangle("right"),
            colour_have_updates=fg,
            colour_no_updates=fg,
            display_format="{updates} updates  ",
            distro="Arch_checkupdates",
            initial_text="No updates  ",
            no_update_string="No updates  ",
            padding=0,
            update_interval=3600,
        ),
    ]


def window_name(bg, fg) -> object:
    return widget.WindowName(
        **base(bg, fg),
        format="{name}",
        max_chars=60,
        width=CALCULATED,
    )


def cpu(bg, fg) -> list:
    return [
        modify(
            TextBox,
            **base(bg, fg),
            **icon_font(),
            **rectangle("left"),
            offset=3,
            text="󰍛",
            x=5,
        ),
        widget.CPU(
            **base(bg, fg),
            **powerline("arrow_right"),
            format="{load_percent:.0f}%",
        ),
    ]


def ram(bg, fg) -> list:
    return [
        TextBox(
            **base(bg, fg),
            **icon_font(),
            offset=-2,
            padding=5,
            text="󰘚",
            x=-2,
        ),
        widget.Memory(
            **base(bg, fg),
            **powerline("arrow_right"),
            format="{MemUsed: .0f}{mm} ",
            padding=-1,
        ),
    ]


def disk(bg, fg) -> list:
    return [
        TextBox(
            **base(bg, fg),
            **icon_font(),
            offset=-1,
            text="",
            x=-5,
        ),
        widget.DF(
            **base(bg, fg),
            **rectangle("right"),
            format="{f} GB  ",
            padding=0,
            partition="/",
            visible_on_warn=False,
            warn_color=fg,
        ),
    ]


def clock(bg, fg) -> list:
    return [
        modify(
            TextBox,
            **base(bg, fg),
            **icon_font(),
            **rectangle("left"),
            offset=2,
            text="",
            x=4,
        ),
        modify(
            Clock,
            **base(bg, fg),
            **rectangle("right"),
            format="%A - %I:%M %p ",
            long_format="%B %-d, %Y ",
            padding=6,
        ),
    ]


widgets = [
    widget.Spacer(length=2),
    logo(color["blue"], color["bg"]),
    sep(color["black"], offset=-8),
    groups(None),
    sep(color["black"], offset=4, padding=4),
    *volume(color["magenta"], color["bg"]),
    *updates(color["red"], color["bg"]),
    widget.Spacer(),
    window_name(None, color["fg"]),
    widget.Spacer(),
    *cpu(color["green"], color["bg"]),
    *ram(color["yellow"], color["bg"]),
    *disk(color["cyan"], color["bg"]),
    sep(color["black"]),
    *clock(color["magenta"], color["bg"]),
    widget.Spacer(length=2),
]
