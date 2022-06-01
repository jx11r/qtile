from libqtile import drawer

def framed(self, border_width, border_color, pad_x, pad_y, highlight_color=None):
    return TextFrame(
        self, border_width, border_color, pad_x, pad_y, highlight_color=highlight_color
    )

class TextFrame(drawer.TextFrame):
    def __init__(self, layout, border_width, border_color, pad_x, pad_y, highlight_color=None):
        super().__init__(layout, border_width, border_color, pad_x, pad_y, highlight_color)

    def draw(self, x, y, rounded=True, fill=False, line=False, highlight=False):
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

            # change to only fill in bottom line
            opts[1] = self.height - self.border_width  # y
            opts[3] = self.border_width  # height

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
