from libqtile.core.manager import Qtile

def bring_to_front(qtile: Qtile) -> None:
  for window in qtile.current_group.windows:
    if window.floating:
      window.cmd_bring_to_front()
