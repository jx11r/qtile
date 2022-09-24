from libqtile.widget import clock

class Clock(clock.Clock):
  defaults = [
    (
      'long_format',
      '%A %d %B %Y | %H:%M',
      'Format to show when widget is clicked.',
    ),
  ]

  def __init__(self, **config):
    super().__init__(**config)
    self.add_defaults(Clock.defaults)
    self.short_format = self.format
    self.toggled = False
    self.add_callbacks(
      { 'Button1': self.toggle }
    )

  def toggle(self):
    if self.toggled:
      self.format = self.short_format
    else:
      self.format = self.long_format

    self.toggled = not self.toggled
    self.update(self.poll())
