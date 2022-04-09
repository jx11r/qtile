# --==[ Widgets ]==--

from libqtile import widget

from utils.settings import city, font, location
from utils.settings import backlight, net
from utils.colors import color

icon_font = 'SauceCodePro Nerd Font'

# General bar settings
widget_defaults = dict(
    font = font,
    fontsize = 10,
    padding = 4,
)
extension_defaults = widget_defaults.copy()

# Functions
def base(bg, fg):
    return {
        'background': bg,
        'foreground': fg,
    }

def font_config(fontsize):
    return {
        'font': icon_font,
        'fontsize': fontsize,
    }

def spacer(bg):
    return widget.Spacer(background = bg)

def sep(fg):
    if fg != '#':
        return widget.TextBox(
            **base(None, fg),
            **font_config(16),
            padding = 12,
            text = '')
    else:
        fg = '#000000'
        return widget.TextBox(
            **base(None, fg),
            **font_config(6),
            padding = 1,
            text = ' ')

def side(fg, side):
    if side.lower() == 'l':
        return widget.TextBox(
            **base(None, fg),
            **font_config(20),
            padding = 0,
            text = '')
    elif side.lower() == 'r':
        return widget.TextBox(
            **base(None, fg),
            **font_config(20),
            padding = 0,
            text = '')

def fix_padding(bg):
    return widget.TextBox(
        **font_config(11),
        background = bg,
        padding = -1,
        text = ' ')

def icon(bg, fg, icon):
    return widget.TextBox(
        **base(bg, fg),
        **font_config(15),
        padding = 3,
        text = icon)

def alt_fg(fg, icon_fg):
    if icon_fg == '#':
        return fg
    else:
        return icon_fg

# Widgets
def layout_icon():
    return widget.CurrentLayoutIcon(
        background = None,
        padding = 7,
        scale = 0.7)

def padding():
    return widget.TextBox(
        **font_config(6),
        background = None,
        padding = 1,
        text = ' ')

def system_tray():
    return widget.Systray(
        background = None,
        icon_size = 15,
        padding = 7)

# Modules
def battery(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        widget.Battery(
            **base(bg, icon_fg),
            **font_config(15),
            format = '{char}',
            charge_char = 'ﮣ',
            discharge_char = ' ',
            full_char = '',
            low_percentage = 0.3,
            low_foreground = color[1],
            padding = None,
            update_interval = 60),
        widget.Battery(
            **base(bg, fg),
            format = '{percent:2.0%}',
            low_foreground = fg,
            padding = None,
            update_interval = 60),
        side(bg, 'R'),
    ]

def brightness(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ' '),
        widget.Backlight(
            **base(bg, fg),
            backlight_name = backlight,
            format = '{percent:2.0%}',
            padding = 0,
            update_interval = 0.2),
        fix_padding(bg),
        side(bg, 'R'),
    ]

def clock(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ' '),
        widget.Clock(
            **base(bg, fg),
            format = '%A, %b %-d, %I:%M %p',
            padding = 0,
            update_interval = 1.0),
        fix_padding(bg),
        side(bg, 'R'),
    ]

def cpu(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ''),
        widget.CPU(
            **base(bg, fg),
            format = '{load_percent:.0f}%',
            padding = None,
            update_interval = 1.0),
        side(bg, 'R'),
    ]

def disk(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ''),
        widget.DF(
            **base(bg, fg),
            format = '{uf}{m}',
            measure = 'G',
            padding = None,
            partition = '/',
            update_interval = 60,
            visible_on_warn = False,
            warn_color = color[1]),
        side(bg, 'R'),
    ]

def groups(bg):
    return [
        widget.GroupBox(
            **font_config(15), # 12
            background = bg,
            blockwidth = 0,
            padding = 4, # 1
            margin_y = 3,
            rounded = True,
            hide_unused = False,
            disable_drag = True,
            use_mouse_wheel = False,
            active = color[4],
            inactive = color[5],
            highlight_method = 'text',
            this_current_screen_border = color[2]),
    ]

def group_number(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, '缾'),
        widget.AGroupBox(
            **base(bg, fg),
            borderwidth = 0,
            margin_y = 4,
            padding = 0),
        side(bg, 'R'),
    ]

def layout(bg, fg):
    return [
        side(bg, 'L'),
        widget.CurrentLayout(
            **base(bg, fg),
            padding = None),
        side(bg, 'R'),
    ]

def logo(bg, fg):
    return [
        side(bg, 'L'),
        widget.TextBox(
            **base(bg, fg),
            **font_config(15),
            padding = 10,
            text = ''),
        fix_padding(bg),
        side(bg, 'R'),
    ]

def quick_exit(bg, fg):
    return [
        side(bg, 'L'),
        widget.QuickExit(
            **base(bg, fg),
            **font_config(15),
            countdown_format='{}',
            countdown_start = 5,
            default_text = '襤',
            padding = 10,
            timer_interval = 1),
        side(bg, 'R'),
    ]

def ram(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, '﬙'),
        widget.Memory(
            **base(bg, fg),
            format = '{MemUsed: .0f}{mm}',
            measure_mem = 'M',
            padding = 0,
            update_interval = 1.0),
        fix_padding(bg),
        side(bg, 'R'),
    ]

def volume(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ''),
        widget.PulseVolume(
            **base(bg, fg),
            get_volume_command = None,
            limit_max_volume = True,
            padding = None,
            update_interval = 0.2),
        side(bg, 'R'),
    ]

def updates(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ' '),
        widget.CheckUpdates(
            **base(bg, fg),
            colour_have_updates = fg,
            colour_no_updates = fg,
            display_format = '{updates}',
            distro = 'Arch_checkupdates',
            no_update_string = '0',
            padding = 0,
            update_interval = 3600),
        fix_padding(bg),
        side(bg, 'R'),
    ]

def spotify(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, '阮 '),
        widget.Mpris2(
            **base(bg, fg),
            name = 'spotify',
            objname = 'org.mpris.MediaPlayer2.spotify',
            display_metadata = ['xesam:title'],
            max_chars = 41,
            padding = 0,
            scroll_chars = None,
            scroll_interval = 0.5,
            stop_pause_text = 'Paused'),
        fix_padding(bg),
        side(bg, 'R'),
    ]

def temp(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ''),
        widget.ThermalSensor(
            **base(bg, fg),
            foreground_alert = color[1],
            metric = True,
            padding = None,
            show_tag = False,
            tag_sensor = None,
            threshold = 80,
            update_interval = 2),
        side(bg, 'R'),
    ]

def weather(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ''),
        widget.OpenWeather(
            **base(bg, fg),
            format = '{main_temp:.0f}°{units_temperature}',
            location = city,
            metric = True,
            padding = None,
            update_interval = 600),
        side(bg, 'R'),
    ]

def wifi_speed(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ''),
        widget.Net(
            **base(bg, fg),
            format = '{down} {up}',
            interface = net,
            padding = None,
            update_interval = 1,
            use_bits = True),
        side(bg, 'R'),
    ]

def wifi(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, ' '),
        widget.Wlan(
            **base(bg, fg),
            disconnected_message = 'Disconnected',
            format = 'Connected',
            interface = net,
            padding = 0,
            update_interval = 5),
        fix_padding(bg),
        side(bg, 'R'),
    ]

def window_count(bg, fg, icon_fg):
    icon_fg = alt_fg(fg, icon_fg)
    return [
        side(bg, 'L'),
        icon(bg, icon_fg, '类'),
        widget.WindowCount(
            **base(bg, fg),
            padding = None,
            show_zero = True,
            text_format = '{num}'),
        side(bg, 'R'),
    ]

def window_name(bg, fg):
    return [
        widget.WindowName(
            **base(bg, fg),
            empty_group_string = ' ',
            for_current_screen = False,
            format = '{state}{name}',
            max_chars = 0,
            padding = None)
    ]

def wttr(bg, fg):
    return [
        side(bg, 'L'),
        widget.Wttr(
            **base(bg, fg),
            format = '%c%t',
            location = location,
            padding = None,
            units = 'm',
            update_interval = 600),
        side(bg, 'R'),
    ]

# --==[ Widgets & Modules [Resume] ]==--
# Arguments: (1, 2, 3)
  # [1] bg = background
  # [2] fg = foreground
  # [3] icon_fg = icon color

# Widgets:
  # layout_icon()
  # padding()
  # system_tray()
  # spacer(1)
  # sep(1)

# Modules:
  # battery(3)
  # brightness(3)
  # clock(3)
  # cpu(3)
  # disk(3)
  # groups(1)
  # group_number(3)
  # layout(2)
  # logo(2)
  # quick_exit(2)
  # ram(3)
  # volume(3)
  # updates(3)
  # spotify(3)
  # temp()
  # weather(3)
  # wifi_speed(3)
  # wifi(3)
  # window_count(3)
  # window_name(2)
  # wttr(2)
