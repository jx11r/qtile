from os import path
from subprocess import PIPE, Popen

xdg = path.expanduser("~/.config/qtile")


def get():
    if path.exists(xdg):
        return xdg

    process = Popen(
        ["pwd"],
        stdout=PIPE,
        text=True,
    )

    return process.communicate()[0].strip()
