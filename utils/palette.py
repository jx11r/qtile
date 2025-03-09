from dataclasses import dataclass


# https://github.com/catppuccin/catppuccin#-palette
# fmt: off
@dataclass(frozen=True)
class Catppuccin:
    rosewater = "#f5e0dc"
    flamingo  = "#f2cdcd"
    pink      = "#f5c2e7"
    mauve     = "#cba6f7"
    red       = "#f38ba8"
    maroon    = "#eba0ac"
    peach     = "#fab387"
    yellow    = "#f9e2af"
    green     = "#a6e3a1"
    teal      = "#94e2d5"
    sky       = "#89dceb"
    sapphire  = "#74c7ec"
    blue      = "#89b4fa"
    lavender  = "#b4befe"
    text      = "#cdd6f4"
    subtext1  = "#bac2de"
    subtext0  = "#a6adc8"
    overlay2  = "#9399b2"
    overlay1  = "#7f849c"
    overlay0  = "#6c7086"
    surface2  = "#585b70"
    surface1  = "#45475a"
    surface0  = "#313244"
    base      = "#1e1e2e"
    mantle    = "#181825"
    crust     = "#11111b"

# https://user-images.githubusercontent.com/58662350/213884019-cbcd5f00-5bef-4a37-9139-0570770330b6.png
@dataclass(frozen=True)
class GruvboxMaterial:
    base   = "#282828"
    black  = "#45403d"
    text   = "#ddc7a1"
    red    = "#ea6962"
    orange = "#e78a4e"
    yellow = "#d8a657"
    green  = "#a9b665"
    aqua   = "#89b482"
    blue   = "#7daea3"
    purple = "#d3869b"
    grey   = "#7c6f64"

palette = GruvboxMaterial()
