import subprocess

from libqtile import bar
from libqtile.widget import base

class Volume(base._TextBox):
  orientations = base.ORIENTATION_HORIZONTAL
  defaults = [
    ('padding', 3, 'Padding left and right. Calculated if None.'),
    ('update_interval', 0.2, 'Update time in seconds.'),
    ('mute_cmd', None, 'Mute command.'),
    ('increase_cmd', None, 'Volume up command.'),
    ('decrease_cmd', None, 'Volume down command.'),
    ('get_volume_cmd', None, 'Command to get the current volume.'),
  ]

  def __init__(self, text = '0', width = bar.CALCULATED, **config):
    super().__init__(text, width, **config)
    self.add_defaults(Volume.defaults)
    self.volume = None

    self.add_callbacks(
      {
        'Button1': self.mute,
        'Button4': self.increase,
        'Button5': self.decrease,
      }
    )

  def timer_setup(self):
    self.timeout_add(self.update_interval, self.update)

  def button_press(self, x, y, button):
    super().button_press(x, y, button)
    self.draw()

  def get_volume(self):
    try:
      command = self.get_volume_cmd
      output = self.call_process(command, shell = True)
      if 'muted' in output.lower():
        output = 'M'
      return output.strip()
    except subprocess.CalledProcessError:
      return -1

  def update(self):
    volume = self.get_volume()
    if volume != self.volume:
      self.volume = volume
      if self.volume == -1:
        self.text = 'M'
      else:
        self.text = self.volume
      self.bar.draw()
    self.timeout_add(self.update_interval, self.update)

  def mute(self):
    if self.mute_cmd is not None:
      subprocess.call(self.mute_cmd, shell = True)

  def increase(self):
    if self.increase_cmd is not None:
      subprocess.call(self.increase_cmd, shell = True)

  def decrease(self):
    if self.decrease_cmd is not None:
      subprocess.call(self.decrease_cmd, shell = True)
