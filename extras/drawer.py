from libqtile import drawer

def framed(self, border_width, border_color, pad_x, pad_y, highlight_color=None):
  return TextFrame(
    self, border_width, border_color, pad_x, pad_y, highlight_color=highlight_color
  )

class TextFrame(drawer.TextFrame):
  def __init__(self, layout, border_width, border_color, pad_x, pad_y, highlight_color=None):
    super().__init__(layout, border_width, border_color, pad_x, pad_y, highlight_color)

  def draw(self, x, y, rounded=True, fill=False, line=False, highlight=False, invert=False):
    self.drawer.set_source_rgb(self.border_color)
    opts = [
      x,
      y,
      self.layout.width + self.pad_left + self.pad_right,
      self.layout.height + self.pad_top + self.pad_bottom,
      self.border_width,
    ]
    if line:
      if highlight:
        self.drawer.set_source_rgb(self.highlight_color)
        self.drawer.fillrect(*opts)
        self.drawer.set_source_rgb(self.border_color)

      opts[1] = 0 if invert else self.height - self.border_width
      opts[3] = self.border_width

      self.drawer.fillrect(*opts)
    elif fill:
      if rounded:
        self.drawer.rounded_fillrect(*opts)
      else:
        self.drawer.fillrect(*opts)
    else:
      if rounded:
        self.drawer.rounded_rectangle(*opts)
      else:
        self.drawer.rectangle(*opts)
    self.drawer.ctx.stroke()
    self.layout.draw(x + self.pad_left, y + self.pad_top)

  def draw_line(self, x, y, highlighted, inverted):
    self.draw(x, y, line=True, highlight=highlighted, invert=inverted)
