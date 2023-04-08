from libqtile.core.manager import Qtile


def float_to_front(qtile: Qtile) -> None:
    for window in qtile.current_group.windows:
        if window.floating:
            window.bring_to_front()
