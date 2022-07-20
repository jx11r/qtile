from libqtile.widget import check_updates

class CheckUpdates(check_updates.CheckUpdates):
  defaults = [
    ('initial_text', '', 'Initial text to display.')
  ]

  def __init__(self, **config):
    super().__init__(**config)
    self.add_defaults(CheckUpdates.defaults)
    self.text = self.initial_text
