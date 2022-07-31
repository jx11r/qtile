import math

from libqtile import bar
from libqtile.widget import textbox

class TextBox(textbox.TextBox):
  def __init__(
    self,
    offset = 0,
    text = ' ',
    width = bar.CALCULATED,
    x = 0,
    y = 0,
    **config,
  ):
    super().__init__(text, width, **config)
    self.add_offset = offset
    self.add_x = x
    self.add_y = y

  def calculate_length(self):
    if self.text:
      if self.bar.horizontal:
        return min(self.layout.width, self.bar.width) \
          + self.actual_padding * 2 + self.add_offset
      else:
        return min(self.layout.width, self.bar.height) \
          + self.actual_padding * 2 + self.add_offset
    else:
      return 0

  def draw(self):
    if not self.can_draw():
      return
    self.drawer.clear(self.background or self.bar.background)

    # size = self.bar.height if self.bar.horizontal else self.bar.width
    self.drawer.ctx.save()

    if not self.bar.horizontal:
      # Left bar reads bottom to top
      if self.bar.screen.left is self.bar:
        self.drawer.ctx.rotate(-90 * math.pi / 180.0)
        self.drawer.ctx.translate(-self.length, 0)

      # Right bar is top to bottom
      else:
        self.drawer.ctx.translate(self.bar.width, 0)
        self.drawer.ctx.rotate(90 * math.pi / 180.0)

    # If we're scrolling, we clip the context to the scroll width less the padding
    # Move the text layout position (and we only see the clipped portion)
    if self._should_scroll:
      self.drawer.ctx.rectangle(
        self.actual_padding,
        0,
        self._scroll_width - 2 * self.actual_padding,
        self.bar.size,
      )
      self.drawer.ctx.clip()

    size = self.bar.height if self.bar.horizontal else self.bar.width

    self.layout.draw(
      (self.actual_padding or 0) - self._scroll_offset + self.add_x,
      int(size / 2.0 - self.layout.height / 2.0) + 1 + self.add_y,
    )
    self.drawer.ctx.restore()

    self.drawer.draw(
      offsetx=self.offsetx, offsety=self.offsety, width=self.width, height=self.height
    )

    # We only want to scroll if:
    # - User has asked us to scroll and the scroll width is smaller than the layout (should_scroll=True)
    # - We are still scrolling (is_scrolling=True)
    # - We haven't already queued the next scroll (scroll_queued=False)
    if self._should_scroll and self._is_scrolling and not self._scroll_queued:
      self._scroll_queued = True
      if self._scroll_offset == 0:
        interval = self.scroll_delay
      else:
        interval = self.scroll_interval
      self._scroll_timer = self.timeout_add(interval, self.do_scroll)
