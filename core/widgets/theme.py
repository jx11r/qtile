from importlib import import_module
from utils import config

theme = {
  'decorated': 'decorated',
}.get(config['bar'], 'decorated')

module = import_module(f'core.widgets.{theme}')
module.bar.update(
  { 'widgets': module.widgets }
)

bar = (module.bar, module.tags)
