# --==[ Colors ]==--

import json
from utils import dir

FILE: str = 'catppuccin'
PATH = f'{dir.get()}/utils/colors/{FILE}.json'

with open(PATH) as file:
  color = json.load(file)
  file.close()

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
