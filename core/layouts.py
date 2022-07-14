# --==[ Layouts ]==--

from libqtile import layout
from libqtile.config import Match

from utils import color

# ---- Tiling ---------------------------- #
config = {
  'single_border_width': 0,
  'border_width': 0,
  'single_margin': 10,
  'margin': 10,
  'border_normal': color[17],
  'border_focus': color[5],
}

layouts = [
  layout.MonadTall(
    **config,
    min_ratio = 0.30,
    max_ratio = 0.70,
    change_ratio = 0.02,
  ),

  layout.Max(**config),
]

# ---- Floating -------------------------- #
floating_layout = layout.Floating(
  fullscreen_border_width = 0,
  border_width = 0,
  border_normal = color[17],
  border_focus = color[7],

  float_rules = [
    *layout.Floating.default_float_rules,
    Match(wm_class = [
      'confirmreset',
      'gnome-screenshot',
      'lxappearance',
      'makebranch',
      'maketag',
      'ssh-askpass',
      'thunar',
      'Xephyr',
      'xfce4-about',
    ]), # type: ignore

    Match(title = [
      'branchdialog',
      'File Operation Progress',
      'minecraft-launcher',
      'Open File',
      'pinentry',
    ]), # type: ignore
  ],
)
