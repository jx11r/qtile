# --==[ Groups ]==--

from libqtile.config import Group, Key, Match
from libqtile.lazy import lazy

from ..utils.settings import mod
from .keys import keys

# Icons & Labels
text = ['term', 'www', 'dev', 'sys', 'vbox', 'doc', 'vid', 'mus', 'chat']
kanji = ['一', '二', '三', '四', '五', '六', '七', '八', '九']
icons = ['', '', '', '', '', '', '辶', '', '切']
numbers = [i for i in range(9)]
circles = ['●'] * 9

label = circles

# Workspaces
groups = [
    Group('1',
        label = label[0],
        layout = 'monadtall',
        matches = [
            Match(title = 'nvim')
        ]),

    Group('2',
        label = label[1],
        layout = 'stack',
        matches = [
            Match(wm_class = ['firefox', 'chromium', 'qutebrowser'])
        ]),

    Group('3',
        label = label[2],
        layout = 'monadtall',
        matches = [
            Match(wm_class = ['code', 'vscodium', 'emacs'])
        ]),

    Group('4',
        label = label[3],
        layout = 'monadtall',
        matches = [
            Match(wm_class = 'thunar'),
            Match(title = 'ranger'),
        ]),

    Group('5',
        label = label[4],
        layout = 'stack',
        matches = [
            Match(wm_class = 'VirtualBox Manager')
        ]),

    Group('6',
        label = label[5],
        layout = 'monadtall',
        matches = [
            Match(wm_class = ['evince', 'libreoffice'])
        ]),

    Group('7',
        label = label[6],
        layout = 'monadtall',
        matches = [
            Match(wm_class = ['obs', 'qBittorrent'])
        ]),

    Group('8',
        label = label[7],
        layout = 'stack',
        matches = [
            Match(wm_class = ['spotify', 'Mplayer', 'vlc'])
        ]),

    Group('9',
        label = label[8],
        layout = 'monadtall',
        matches = [
            Match(wm_class = ['telegram-desktop', 'discord', 'caprine']),
            Match(title = 'WhatsApp Web'),
        ]),
]

# Navigation
for i in groups:
    keys.extend([
        # Switch to group {}
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle = True)),

        # Move focused window to group {}
        Key([mod, 'shift'], i.name, lazy.window.togroup(i.name)),
    ])
