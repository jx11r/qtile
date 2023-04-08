import json

from utils import dir

directory = f"{dir.get()}/config.json"

settings = {
    "bar": "decorated",
    "browser": "",
    "colorscheme": "catppuccin",
    "terminal": {
        "main": "",
        "floating": "",
    },
    "wallpaper": "~/wallpaper/wp.png",
}

try:
    with open(directory, "r") as file:
        config = json.load(file)
except FileNotFoundError:
    with open(directory, "w") as file:
        file.write(json.dumps(settings, indent=4))
        config = settings.copy()
