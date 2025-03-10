import math

from libqtile import bar
from libqtile.widget import base, textbox


class _TextBox(base._TextBox):
    def __init__(self, text=" ", width=bar.CALCULATED, **config):
        super().__init__(text, width, **config)
        self.add_offset = config.pop("offset", 0)
        self.add_x = config.pop("x", 0)
        self.add_y = config.pop("y", 0)

    def calculate_length(self):
        if self.text:
            if self.bar.horizontal:
                return (
                    min(self.layout.width, self.bar.width)
                    + self.actual_padding * 2
                    + self.add_offset
                )
            else:
                if self.rotate:
                    return (
                        min(self.layout.width, self.bar.height)
                        + self.actual_padding * 2
                    )
                else:
                    return self.layout.height + self.actual_padding * 2
        else:
            return 0

    def draw(self):
        if not self.can_draw():
            return
        self.drawer.clear(self.background or self.bar.background)

        # size = self.bar.height if self.bar.horizontal else self.bar.width
        self.drawer.ctx.save()

        if not self.bar.horizontal and self.rotate:
            # Left bar reads bottom to top
            # Can be overriden to read bottom to top all the time with vertical_text_direction
            if (
                self.bar.screen.left is self.bar and self.direction == "default"
            ) or self.direction == "btt":
                self.drawer.ctx.rotate(-90 * math.pi / 180.0)
                self.drawer.ctx.translate(-self.length, 0)

            # Right bar is top to bottom
            # Can be overriden to read top to bottom all the time with vertical_text_direction
            elif (
                self.bar.screen.right is self.bar and self.direction == "default"
            ) or self.direction == "ttb":
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

        if self.bar.horizontal:
            size = self.bar.height
        else:
            if self.rotate:
                size = self.bar.width
            else:
                size = self.layout.height + self.actual_padding * 2

        self.layout.draw(
            (self.actual_padding or 0) - self._scroll_offset + self.add_x,
            int(size / 2.0 - self.layout.height / 2.0) + 1 + self.add_y,
        )
        self.drawer.ctx.restore()

        self.drawer.draw(
            offsetx=self.offsetx,
            offsety=self.offsety,
            width=self.width,
            height=self.height,
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


class TextBox(_TextBox, textbox.TextBox):
    def __init__(self, text=" ", width=bar.CALCULATED, **config):
        super().__init__(text, width, **config)
