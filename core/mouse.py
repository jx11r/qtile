from libqtile.config import Click, Drag
from libqtile.lazy import lazy

from core.keys import mod

mouse = [
  # Left click
  Drag(
    [mod],
    'Button1',
    lazy.window.set_position_floating(),
    start = lazy.window.get_position(),
  ),

  # Right click
  Drag(
    [mod],
    'Button3',
    lazy.window.set_size_floating(),
    start = lazy.window.get_size(),
  ),

  # Scroll wheel
  Click(
    [mod],
    'Button2',
    lazy.window.bring_to_front(),
  ),
]
