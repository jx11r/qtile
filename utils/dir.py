from os import path
from subprocess import Popen, PIPE

xdg = '.config/qtile'
home = path.expanduser('~')

def get() -> str:
  try:
    open(f'{home}/{xdg}/config.py', 'r').close()
    return f'{home}/{xdg}'
  except FileNotFoundError:
    process = Popen(
      ['pwd'],
      stdout = PIPE,
      text = True,
    )
    return process.communicate()[0].strip()
