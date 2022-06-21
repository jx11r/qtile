# --==[ Current Directory ]==--

from os import path
from subprocess import Popen, PIPE

XDG = '.config/qtile'

def get() -> str:
    process = Popen(
        ['pwd'],
        stdout = PIPE,
        text = True,
    )
    output = process.communicate()[0].strip()

    if path.expanduser('~') == output:
        return f'{output}/{XDG}'
    else:
        return output
