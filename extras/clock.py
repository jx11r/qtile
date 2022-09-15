from libqtile.widget import clock

class Clock(clock.Clock):
  defaults = [
    (
      'long_format',
      '%A %d %B %Y | %H:%M',
      'Format to show when mouse is over widget.',
    ),
  ]

  def __init__(self, **config):
    super().__init__(**config)
    self.add_defaults(Clock.defaults)
    self.short_format = self.format

  def mouse_enter(self, *args, **kwargs):
    self.format = self.long_format
    self.bar.draw()

  def mouse_leave(self, *args, **kwargs):
    self.format = self.short_format
    self.bar.draw()
