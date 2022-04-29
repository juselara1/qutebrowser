class GruvboxDarkHard():
    base00 = "#1d2021"
    base01 = "#3c3836"
    base02 = "#504945"
    base03 = "#665c54"
    base04 = "#bdae93"
    base05 = "#d5c4a1"
    base06 = "#ebdbb2"
    base07 = "#fbf1c7"
    base08 = "#fb4934"
    base09 = "#fe8019"
    base0A = "#fabd2f"
    base0B = "#b8bb26"
    base0C = "#8ec07c"
    base0D = "#83a598"
    base0E = "#d3869b"
    base0F = "#d65d0e"

class GruvboxDarkMedium():
    base00 = "#282828"
    base01 = "#3c3836"
    base02 = "#504945"
    base03 = "#665c54"
    base04 = "#bdae93"
    base05 = "#d5c4a1"
    base06 = "#ebdbb2"
    base07 = "#fbf1c7"
    base08 = "#fb4934"
    base09 = "#fe8019"
    base0A = "#fabd2f"
    base0B = "#b8bb26"
    base0C = "#8ec07c"
    base0D = "#83a598"
    base0E = "#d3869b"
    base0F = "#d65d0e"

class GruvboxDarkPale():
    base00 = "#262626"
    base01 = "#3a3a3a"
    base02 = "#4e4e4e"
    base03 = "#8a8a8a"
    base04 = "#949494"
    base05 = "#dab997"
    base06 = "#d5c4a1"
    base07 = "#ebdbb2"
    base08 = "#d75f5f"
    base09 = "#ff8700"
    base0A = "#ffaf00"
    base0B = "#afaf00"
    base0C = "#85ad85"
    base0D = "#83adad"
    base0E = "#d485ad"
    base0F = "#d65d0e"

class GruvboxDarkSoft():
    base00 = "#32302f"
    base01 = "#3c3836"
    base02 = "#504945"
    base03 = "#665c54"
    base04 = "#bdae93"
    base05 = "#d5c4a1"
    base06 = "#ebdbb2"
    base07 = "#fbf1c7"
    base08 = "#fb4934"
    base09 = "#fe8019"
    base0A = "#fabd2f"
    base0B = "#b8bb26"
    base0C = "#8ec07c"
    base0D = "#83a598"
    base0E = "#d3869b"
    base0F = "#d65d0e"

class GruvBoxLightHard():
    base00 = "#f9f5d7"
    base01 = "#ebdbb2"
    base02 = "#d5c4a1"
    base03 = "#bdae93"
    base04 = "#665c54"
    base05 = "#504945"
    base06 = "#3c3836"
    base07 = "#282828"
    base08 = "#9d0006"
    base09 = "#af3a03"
    base0A = "#b57614"
    base0B = "#79740e"
    base0C = "#427b58"
    base0D = "#076678"
    base0E = "#8f3f71"
    base0F = "#d65d0e"

class GruvBoxLightMedium():
    base00 = "#fbf1c7"
    base01 = "#ebdbb2"
    base02 = "#d5c4a1"
    base03 = "#bdae93"
    base04 = "#665c54"
    base05 = "#504945"
    base06 = "#3c3836"
    base07 = "#282828"
    base08 = "#9d0006"
    base09 = "#af3a03"
    base0A = "#b57614"
    base0B = "#79740e"
    base0C = "#427b58"
    base0D = "#076678"
    base0E = "#8f3f71"
    base0F = "#d65d0e"

class GruvBoxLightPale():
    base00 = "#f2e5bc"
    base01 = "#ebdbb2"
    base02 = "#d5c4a1"
    base03 = "#bdae93"
    base04 = "#665c54"
    base05 = "#504945"
    base06 = "#3c3836"
    base07 = "#282828"
    base08 = "#9d0006"
    base09 = "#af3a03"
    base0A = "#b57614"
    base0B = "#79740e"
    base0C = "#427b58"
    base0D = "#076678"
    base0E = "#8f3f71"
    base0F = "#d65d0e"

class GruvBox(object):
    def __init__(self, c, gruvtype):
        self.gruvtype = gruvtype
        self.c = c
    
    def __call__(self):
        if self.gruvtype == "dark_hard":
            self.set(GruvboxDarkHard)
        elif self.gruvtype == "dark_medium":
            self.set(GruvboxDarkMedium)
        elif self.gruvtype == "dark_pale":
            self.set(GruvboxDarkPale)
        elif self.gruvtype == "dark_soft":
            self.set(GruvboxDarkSoft)
        if self.gruvtype == "light_hard":
            self.set(GruvboxLightHard)
        elif self.gruvtype == "light_medium":
            self.set(GruvboxLightMedium)
        elif self.gruvtype == "light_soft":
            self.set(GruvboxLightSoft)

    def set(self, gruvtype):
        self.c.colors.completion.fg = gruvtype.base05
        self.c.colors.completion.odd.bg = gruvtype.base01
        self.c.colors.completion.even.bg = gruvtype.base00
        self.c.colors.completion.category.fg = gruvtype.base0A
        self.c.colors.completion.category.bg = gruvtype.base00
        self.c.colors.completion.category.border.top = gruvtype.base00
        self.c.colors.completion.category.border.bottom = gruvtype.base00
        self.c.colors.completion.item.selected.fg = gruvtype.base05
        self.c.colors.completion.item.selected.bg = gruvtype.base02
        self.c.colors.completion.item.selected.border.top = gruvtype.base02
        self.c.colors.completion.item.selected.border.bottom = gruvtype.base02
        self.c.colors.completion.item.selected.match.fg = gruvtype.base0B
        self.c.colors.completion.match.fg = gruvtype.base0B
        self.c.colors.completion.scrollbar.fg = gruvtype.base05
        self.c.colors.completion.scrollbar.bg = gruvtype.base00
        self.c.colors.contextmenu.menu.bg = gruvtype.base00
        self.c.colors.contextmenu.menu.fg =  gruvtype.base05
        self.c.colors.contextmenu.selected.bg = gruvtype.base02
        self.c.colors.contextmenu.selected.fg = gruvtype.base05
        self.c.colors.downloads.bar.bg = gruvtype.base00
        self.c.colors.downloads.start.fg = gruvtype.base00
        self.c.colors.downloads.start.bg = gruvtype.base0D
        self.c.colors.downloads.stop.fg = gruvtype.base00
        self.c.colors.downloads.stop.bg = gruvtype.base0C
        self.c.colors.downloads.error.fg = gruvtype.base08
        self.c.colors.hints.fg = gruvtype.base00
        self.c.colors.hints.bg = gruvtype.base0A
        self.c.colors.hints.match.fg = gruvtype.base05
        self.c.colors.keyhint.fg = gruvtype.base05
        self.c.colors.keyhint.suffix.fg = gruvtype.base05
        self.c.colors.keyhint.bg = gruvtype.base00
        self.c.colors.messages.error.fg = gruvtype.base00
        self.c.colors.messages.error.bg = gruvtype.base08
        self.c.colors.messages.error.border = gruvtype.base08
        self.c.colors.messages.warning.fg = gruvtype.base00
        self.c.colors.messages.warning.bg = gruvtype.base0E
        self.c.colors.messages.warning.border = gruvtype.base0E
        self.c.colors.messages.info.fg = gruvtype.base05
        self.c.colors.messages.info.bg = gruvtype.base00
        self.c.colors.messages.info.border = gruvtype.base00
        self.c.colors.prompts.fg = gruvtype.base05
        self.c.colors.prompts.border = gruvtype.base00
        self.c.colors.prompts.bg = gruvtype.base00
        self.c.colors.prompts.selected.bg = gruvtype.base02
        self.c.colors.statusbar.normal.fg = gruvtype.base0B
        self.c.colors.statusbar.normal.bg = gruvtype.base00
        self.c.colors.statusbar.insert.fg = gruvtype.base00
        self.c.colors.statusbar.insert.bg = gruvtype.base0D
        self.c.colors.statusbar.passthrough.fg = gruvtype.base00
        self.c.colors.statusbar.passthrough.bg = gruvtype.base0C
        self.c.colors.statusbar.private.fg = gruvtype.base00
        self.c.colors.statusbar.private.bg = gruvtype.base01
        self.c.colors.statusbar.command.fg = gruvtype.base05
        self.c.colors.statusbar.command.bg = gruvtype.base00
        self.c.colors.statusbar.command.private.fg = gruvtype.base05
        self.c.colors.statusbar.command.private.bg = gruvtype.base00
        self.c.colors.statusbar.caret.fg = gruvtype.base00
        self.c.colors.statusbar.caret.bg = gruvtype.base0E
        self.c.colors.statusbar.caret.selection.fg = gruvtype.base00
        self.c.colors.statusbar.caret.selection.bg = gruvtype.base0D
        self.c.colors.statusbar.progress.bg = gruvtype.base0D
        self.c.colors.statusbar.url.fg = gruvtype.base05
        self.c.colors.statusbar.url.error.fg = gruvtype.base08
        self.c.colors.statusbar.url.hover.fg = gruvtype.base05
        self.c.colors.statusbar.url.success.http.fg = gruvtype.base0C
        self.c.colors.statusbar.url.success.https.fg = gruvtype.base0B
        self.c.colors.statusbar.url.warn.fg = gruvtype.base0E
        self.c.colors.tabs.bar.bg = gruvtype.base00
        self.c.colors.tabs.indicator.start = gruvtype.base0D
        self.c.colors.tabs.indicator.stop = gruvtype.base0C
        self.c.colors.tabs.indicator.error = gruvtype.base08
        self.c.colors.tabs.odd.fg = gruvtype.base05
        self.c.colors.tabs.odd.bg = gruvtype.base01
        self.c.colors.tabs.even.fg = gruvtype.base05
        self.c.colors.tabs.even.bg = gruvtype.base00
        self.c.colors.tabs.pinned.even.bg = gruvtype.base0C
        self.c.colors.tabs.pinned.even.fg = gruvtype.base07
        self.c.colors.tabs.pinned.odd.bg = gruvtype.base0B
        self.c.colors.tabs.pinned.odd.fg = gruvtype.base07
        self.c.colors.tabs.pinned.selected.even.bg = gruvtype.base02
        self.c.colors.tabs.pinned.selected.even.fg = gruvtype.base05
        self.c.colors.tabs.pinned.selected.odd.bg = gruvtype.base02
        self.c.colors.tabs.pinned.selected.odd.fg = gruvtype.base05
        self.c.colors.tabs.selected.odd.fg = gruvtype.base05
        self.c.colors.tabs.selected.odd.bg = gruvtype.base02
        self.c.colors.tabs.selected.even.fg = gruvtype.base05
        self.c.colors.tabs.selected.even.bg = gruvtype.base02
        self.c.colors.webpage.bg = gruvtype.base00
