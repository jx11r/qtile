import json
from utils import dir

directory = f'{dir.get()}/config.json'
defaults = {
  'bar': 'decorated',
  'browser': 'firefox',
  'colorscheme': 'catppuccin',
  'file_manager': 'thunar',
  'terminal': 'default',
  'wallpaper': '~/wallpapers/wp6.png',
}

try:
  with open(directory, 'r') as file:
    config = json.load(file)
    file.close()
except FileNotFoundError:
  with open(directory, 'w') as file:
    file.write(json.dumps(defaults, indent = 2))
    config = defaults.copy()
    file.close()
