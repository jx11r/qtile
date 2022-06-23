# --==[ Current Directory ]==--

from os import path
from subprocess import Popen, PIPE

XDG: str = '/.config/qtile'
TEST: str = '/config.py'

def get() -> str:
  PATH: str = XDG + TEST
  HOME = path.expanduser('~')

  try:
    open(f'{HOME}{PATH}')
    return HOME + XDG

  except FileNotFoundError:
    process = Popen(
      ['pwd'],
      stdout = PIPE,
      text = True,
    )
    return process.communicate()[0].strip()
