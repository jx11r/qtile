from libqtile import bar
from libqtile.widget import base

class TextBox(base._TextBox):
  '''A flexible textbox that can be updated from bound keys, scripts, and qshell.'''

  def __init__(self, text = ' ', width = bar.CALCULATED, offset = 0, **config):
    base._TextBox.__init__(self, text = text, width = width, **config)
    self.add_offset = offset

  def cmd_update(self, text):
    '''Update the text in a TextBox widget'''
    self.update(text)

  def cmd_get(self):
    '''Retrieve the text in a TextBox widget'''
    return self.text

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
