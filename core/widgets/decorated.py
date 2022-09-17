from libqtile.bar import CALCULATED
from libqtile.lazy import lazy

from core.widgets.base import base, decoration, font, icon, powerline
from extras import Clock, GroupBox, TextBox, Volume
from extras import modify, widget
from utils import color

tags: list[str] = [
  '', '', '', '', '切', '',
]

bar: dict = {
  'background': color['bg'],
  'border_color': color['bg'],
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
      color['cyan'], color['magenta'], color['yellow'],
      color['red'], color['blue'], color['green'],
    ],
    highlight_color = color['bg'],
    highlight_method = 'line',
    inactive = color['black'],
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
    modify(
      Volume,
      **base(bg, fg),
      **powerline('arrow_right'),
      decrease_cmd = 'pamixer --decrease 5',
      increase_cmd = 'pamixer --increase 5',
      get_volume_cmd = 'pamixer --get-volume-human',
      mute_cmd = 'pamixer --toggle-mute',
      update_interval = 0.1,
    ),
  ]

def updates(bg: str, fg: str) -> list:
  return [
    TextBox(
      **icon(bg, fg),
      offset = -1,
      text = '',
      x = -5,
    ),
    widget.CheckUpdates(
      **base(bg, fg),
      **decoration('right'),
      colour_have_updates = fg,
      colour_no_updates = fg,
      display_format = '{updates} updates  ',
      distro = 'Arch_checkupdates',
      initial_text = 'No updates  ',
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
      **powerline('arrow_right'),
      format = '{load_percent:.0f}%',
    )
  ]

def ram(bg: str, fg: str) -> list:
  return [
    TextBox(
      **icon(bg, fg),
      offset = -2,
      padding = 5,
      text = '﬙',
      x = -2,
    ),
    widget.Memory(
      **base(bg, fg),
      **powerline('arrow_right'),
      format = '{MemUsed: .0f}{mm} ',
      padding = -1,
    ),
  ]

def disk(bg: str, fg: str) -> list:
  return [
    TextBox(
      **icon(bg, fg),
      offset = -1,
      text = '',
      x = -5,
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
    modify(
      Clock,
      **base(bg, fg),
      **decoration('right'),
      format = '%A - %I:%M %p ',
      long_format = '%B %-d, %Y ',
      padding = 6,
    ),
  ]

widgets: list = [
  widget.Spacer(length = 4),
  logo(color['blue'], color['bg']),
  sep(color['black'], offset = -8),
  groups(None),
  sep(color['black'], offset = 4, padding = 4),
  *volume(color['magenta'], color['bg']),
  *updates(color['red'], color['bg']),

  widget.Spacer(),
  window_name(None, color['fg']),
  widget.Spacer(),

  *cpu(color['green'], color['bg']),
  *ram(color['yellow'], color['bg']),
  *disk(color['cyan'], color['bg']),
  sep(color['black']),
  *clock(color['magenta'], color['bg']),
  widget.Spacer(length = 4),
]
