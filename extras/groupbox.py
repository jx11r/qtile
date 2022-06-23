from libqtile.widget import groupbox, base
from extras.drawer import framed

class _GroupBase(groupbox._GroupBase):
  def __init__(self, **config):
    super().__init__(**config)

  def _configure(self, qtile, bar):
    base._Widget._configure(self, qtile, bar)

    if self.fontsize is None:
      calc = self.bar.height - self.margin_y * 2 - self.borderwidth * 2 - self.padding_y * 2
      self.fontsize = max(calc, 1)

    self.layout = self.drawer.textlayout(
      "", "ffffff", self.font, self.fontsize, self.fontshadow
    )
    self.layout.framed = framed.__get__(self.layout)
    self.setup_hooks()

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

class GroupBox(_GroupBase, groupbox.GroupBox):
  defaults = [
    ("invert", False, "Invert line position when 'line' highlight method isn't highlighted."),
    ("rainbow", False, "If set to True, 'colors' will be used instead of '*_screen_border'."),
    (
      "colors",
      False,
      "Receive a list of strings."
      "Allows each tag to be an independent/unique color when selected, this overrides 'active'."
    ),
  ]

  def __init__(self, **config):
    super().__init__(**config)
    self.add_defaults(GroupBox.defaults)

  def draw(self):
    self.drawer.clear(self.background or self.bar.background)

    def color(index: int) -> str:
      try:
        return self.colors[index]
      except IndexError:
        return "FFFFFF"

    offset = self.margin_x
    for i, g in enumerate(self.groups):
      to_highlight = False
      is_block = self.highlight_method == "block"
      is_line = self.highlight_method == "line"

      bw = self.box_width([g])

      if self.group_has_urgent(g) and self.urgent_alert_method == "text":
        text_color = self.urgent_text
      elif g.windows:
        text_color = color(i) if self.colors else self.active
      else:
        text_color = self.inactive

      if g.screen:
        if self.highlight_method == "text":
          border = None
          text_color = self.this_current_screen_border
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
        g.label,
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
