import subprocess

from libqtile import bar
from libqtile.widget import base


class Volume(base._TextBox):
    orientations = base.ORIENTATION_HORIZONTAL
    defaults = [
        ("padding", 3, "Padding left and right. Calculated if None."),
        ("update_interval", 0.2, "Update time in seconds."),
    ]

    def __init__(self, commands: dict, text="0%", width=bar.CALCULATED, **config):
        super().__init__(text, width, **config)
        self.add_defaults(Volume.defaults)
        self.vol_commands = commands
        self.volume = None

        self.add_callbacks(
            {
                "Button1": self.mute,
                "Button4": self.increase,
                "Button5": self.decrease,
            }
        )

    def timer_setup(self):
        self.timeout_add(self.update_interval, self.update)

    def button_press(self, x, y, button):
        super().button_press(x, y, button)
        self.draw()

    def get_volume(self):
        try:
            command = self.vol_commands["get"]
            output = self.call_process(command, shell=True)
            if "muted" in output.lower():
                output = "M"
            return output.strip()
        except subprocess.CalledProcessError:
            return -1

    def update(self):
        volume = self.get_volume()
        if volume != self.volume:
            self.volume = volume
            if self.volume == -1:
                self.text = "M"
            else:
                self.text = self.volume
            self.bar.draw()
        self.timeout_add(self.update_interval, self.update)

    def mute(self):
        if "mute" in self.vol_commands:
            subprocess.call(self.vol_commands["mute"], shell=True)

    def increase(self):
        if "increase" in self.vol_commands:
            subprocess.call(self.vol_commands["increase"], shell=True)

    def decrease(self):
        if "decrease" in self.vol_commands:
            subprocess.call(self.vol_commands["decrease"], shell=True)
