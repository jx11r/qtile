from libqtile.widget import check_updates

class CheckUpdates(check_updates.CheckUpdates):
  def __init__(self, initial_text = '', **config):
    super().__init__(**config)
    self.text = initial_text
