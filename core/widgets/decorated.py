# Inspired by Axyl's polybar.
# https://github.com/axyl-os

from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.widgets.base import base, decoration, font, icon
from extras import CheckUpdates, GroupBox, modify, TextBox, widget
from utils import color

tags: list[str] = [
  '', '', '', '', '切', '',
]

bar: dict = {
  'background': color[16],
  'border_color': color[16],
  'border_width': 4,
  'margin': [10, 10, 0, 10],
  'opacity': 1,
  'size': 18,
}

def sep(fg: str, offset = 0, padding = 8) -> TextBox:
  return TextBox(
    **icon(None, fg),
    offset = offset,
    padding = padding,
    text = '',
  )

def powerline(bg: str, color: str) -> TextBox:
  return TextBox(
    **base(bg, color),
    **font(31),
    offset = -1,
    padding = -4,
    text = '',
    y = -1,
  )

def logo(bg: str, fg: str) -> TextBox:
  return modify(
    TextBox,
    **decoration(),
    **icon(bg, fg),
    mouse_callbacks = { 'Button1': lazy.restart() },
    offset = 4,
    padding = 17,
    text = '',
  )

def groups(bg: str) -> GroupBox:
  return GroupBox(
    **font(15),
    background = bg,
    borderwidth = 1,
    colors = [
      color[6], color[5], color[3],
      color[1], color[4], color[2],
    ],
    highlight_color = color[16],
    highlight_method = 'line',
    inactive = color[8],
    invert = True,
    padding = 7,
    rainbow = True,
  )

def volume(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **decoration('left'),
      **icon(bg, fg),
      text = '',
      x = 4,
    ),
    widget.PulseVolume(
      **base(bg, fg),
      update_interval = 0.1,
    ),
  ]

def updates(bg: str, fg: str) -> list:
  return [
    TextBox(
      **icon(bg, fg),
      offset = -2,
      text = '',
      x = -6,
    ),
    modify(
      CheckUpdates,
      **base(bg, fg),
      **decoration('right'),
      colour_have_updates = fg,
      colour_no_updates = fg,
      display_format = '{updates} updates  ',
      distro = 'Arch_checkupdates',
      initial_text = 'Loading...  ',
      no_update_string = 'No updates  ',
      padding = 0,
      update_interval = 3600,
    ),
  ]

def window_name(bg: str, fg: str) -> object:
  return widget.WindowName(
    **base(bg, fg),
    format = '{name}',
    max_chars = 60,
    width = CALCULATED,
  )

def cpu(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **icon(bg, fg),
      **decoration('left'),
      offset = 3,
      text = '',
      x = 5,
    ),
    widget.CPU(
      **base(bg, fg),
      format = '{load_percent:.0f}%',
    )
  ]

def ram(bg: str, fg: str) -> list:
  return [
    TextBox(
      **icon(bg, fg),
      offset = -3,
      padding = 5,
      text = '﬙',
      x = -3,
    ),
    widget.Memory(
      **base(bg, fg),
      format = '{MemUsed: .0f}{mm} ',
      padding = -1,
    ),
  ]

def disk(bg: str, fg: str) -> list:
  return [
    TextBox(
      **icon(bg, fg),
      offset = -2,
      text = '',
      x = -6,
    ),
    widget.DF(
      **base(bg, fg),
      **decoration('right'),
      format = '{f} GB  ',
      padding = 0,
      partition = '/',
      visible_on_warn = False,
      warn_color = fg,
    ),
  ]

def clock(bg: str, fg: str) -> list:
  return [
    modify(
      TextBox,
      **decoration('left'),
      **icon(bg, fg),
      offset = 2,
      text = '',
      x = 4,
    ),
    widget.Clock(
      **base(bg, fg),
      **decoration('right'),
      format = '%A - %I:%M %p ',
      padding = 6,
    ),
  ]

widgets: list = [
  widget.Spacer(length = 4),
  logo(color[4], color[16]),
  sep(color[8], offset = -8),
  groups(None),
  sep(color[8], offset = 4, padding = 4),
  *volume(color[5], color[16]),
  powerline(color[5], color[1]),
  *updates(color[1], color[16]),

  widget.Spacer(),
  window_name(None, color[17]),
  widget.Spacer(),

  *cpu(color[2], color[16]),
  powerline(color[2], color[3]),
  *ram(color[3], color[16]),
  powerline(color[3], color[6]),
  *disk(color[6], color[16]),
  sep(color[8]),
  *clock(color[5], color[16]),
  widget.Spacer(length = 4),
]
