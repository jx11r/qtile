import json

from utils import dir
from utils.settings import config

colorscheme = {
  'catppuccin': 'catppuccin.json',
  'gruvbox_material': 'gruvbox_material.json',
  'material_ocean': 'material_ocean.json',
}.get(config['colorscheme'], 'catppuccin.json')

path = f'{dir.get()}/utils/colorscheme/{colorscheme}'

with open(path, 'r') as file:
  color = json.load(file)
  file.close()
