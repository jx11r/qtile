from libqtile.widget import groupbox, base
from extras.drawer import framed

class GroupBox(groupbox.GroupBox):
  defaults = [
    ("invert", False, "Invert line position when 'line' highlight method isn't highlighted."),
    ("rainbow", False, "If set to True, 'colors' will be used instead of '*_screen_border'."),
    (
      "colors",
      False,
      "Receive a list of strings."
      "Allows each tag to be an independent/unique color when selected, this overrides 'active'."
    ),
    (
      "icons",
      {
        "active": "",
        "empty": "○",
        "occupied": "◉",
      },
      "Will be used in the 'icon' highlight method.",
    )
  ]

  def __init__(self, **config):
    super().__init__(**config)
    self.add_defaults(GroupBox.defaults)

  def _configure(self, qtile, bar):
    super()._configure(qtile, bar)
    self.layout.framed = framed.__get__(self.layout)

  def drawbox(
    self,
    offset,
    text,
    bordercolor,
    textcolor,
    highlight_color=None,
    width=None,
    rounded=False,
    block=False,
    line=False,
    highlighted=False,
    inverted=False,
  ):
    self.layout.text = self.fmt.format(text)
    self.layout.font_family = self.font
    self.layout.font_size = self.fontsize
    self.layout.colour = textcolor
    if width is not None:
      self.layout.width = width
    if line:
      pad_y = [
        (self.bar.height - self.layout.height - self.borderwidth) / 2,
        (self.bar.height - self.layout.height + self.borderwidth) / 2,
      ]
      if highlighted:
        inverted = False
    else:
      pad_y = self.padding_y

    if bordercolor is None:
      # border colour is set to None when we don't want to draw a border at all
      # Rather than dealing with alpha blending issues, we just set border width
      # to 0.
      border_width = 0
      framecolor = self.background or self.bar.background
    else:
      border_width = self.borderwidth
      framecolor = bordercolor

    framed = self.layout.framed(border_width, framecolor, 0, pad_y, highlight_color)
    y = self.margin_y
    if self.center_aligned:
      for t in base.MarginMixin.defaults:
        if t[0] == "margin":
          y += (self.bar.height - framed.height) / 2 - t[1]
          break
    if block and bordercolor is not None:
      framed.draw_fill(offset, y, rounded)
    elif line:
      framed.draw_line(offset, y, highlighted, inverted)
    else:
      framed.draw(offset, y, rounded)

  def draw(self):
    self.drawer.clear(self.background or self.bar.background)

    def color(index: int) -> str:
      try:
        return self.colors[index]
      except IndexError:
        return "FFFFFF"

    offset = self.margin_x
    for i, g in enumerate(self.groups):
      is_block = self.highlight_method == "block"
      is_line = self.highlight_method == "line"
      is_icon = self.highlight_method == "icon"
      to_highlight = False

      bw = self.box_width([g])

      if self.group_has_urgent(g) and self.urgent_alert_method == "text":
        text_color = self.urgent_text
      elif g.windows:
        text_color = color(i) if self.colors else self.active
        icon = self.icons["occupied"]
      else:
        text_color = self.inactive
        icon = self.icons["empty"]

      if g.screen:
        if self.highlight_method == "text":
          border = None
          text_color = self.this_current_screen_border
        elif is_icon:
          icon = self.icons["active"]
          border = None
          text_color = color(i) if self.colors else self.this_current_screen_border
        else:
          if self.block_highlight_text_color:
            text_color = self.block_highlight_text_color

          if self.bar.screen.group.name == g.name:
            if self.qtile.current_screen == self.bar.screen:
              if self.rainbow and self.colors:
                border = color(i) if g.windows else self.inactive
              else:
                border = self.this_current_screen_border
              to_highlight = True
            else:
              if self.rainbow and self.colors:
                border = color(i) if g.windows else self.inactive
              else:
                border = self.this_screen_border
              to_highlight = True

          else:
            if self.qtile.current_screen == g.screen:
              if self.rainbow and self.colors:
                border = color(i) if g.windows else self.inactive
              else:
                border = self.other_current_screen_border
            else:
              if self.rainbow and self.colors:
                border = color(i) if g.windows else self.inactive
              else:
                border = self.other_screen_border

      elif self.group_has_urgent(g) and self.urgent_alert_method in (
        "border",
        "block",
        "line",
      ):
        border = self.urgent_border
        if self.urgent_alert_method == "block":
          is_block = True
        elif self.urgent_alert_method == "line":
          is_line = True
      else:
        border = None

      self.drawbox(
        offset,
        icon if is_icon else g.label,
        border,
        text_color,
        highlight_color=self.highlight_color,
        width=bw,
        rounded=self.rounded,
        block=is_block,
        line=is_line,
        highlighted=to_highlight,
        inverted=self.invert,
      )
      offset += bw + self.spacing
    self.drawer.draw(offsetx=self.offset, offsety=self.offsety, width=self.width)
