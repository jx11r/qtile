# --==[ Colors ]==--

from os import path
import json

from .settings import colorscheme

# Directory
color_file = path.join(
    path.expanduser('~'),
    '.config/qtile/utils/colors/',
    colorscheme + '.json'
)

# Import JSON file
with open(color_file) as file:
    colors = json.load(file)
    file.close()

color = [''] * len(colors)

for key, value in colors.items():
    color[int(key)] = value

# Normal:
  # [0] = black
  # [1] = red
  # [2] = green
  # [3] = yellow
  # [4] = blue
  # [5] = magenta
  # [6] = cyan
  # [7] = white

# Bright:
  # [8]  = black
  # [9]  = red
  # [10] = green
  # [11] = yellow
  # [12] = blue
  # [13] = magenta
  # [14] = cyan
  # [15] = white

# Primary:
  # [16] = background
  # [17] = foreground
