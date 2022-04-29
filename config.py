from qutebrowser.api import interceptor
from plugins.gruvbox.configs import GruvBox
import sys, os

config.load_autoconfig(False)

# gruvbox theme
theme = GruvBox(c, "dark_hard")
theme()

# searchengine
c.url.searchengines = {
        'DEFAULT':  'https://google.com/search?hl=en&q={}',
        '!gh':      'https://github.com/search?o=desc&q={}&s=stars',
        '!w':       'https://en.wikipedia.org/wiki/{}',
        '!yt':      'https://www.youtube.com/results?search_query={}',
        '!gs':      'https://scholar.google.com/scholar?hl=en&q={}'
    }

base_url = "https://google.com/"
c.url.default_page = base_url
c.url.start_pages = [base_url]

# downloads
c.downloads.location.directory = "/home/juselara/repositories/tmp"

# colors
c.colors.webpage.darkmode.enabled = True

# permissions
c.content.autoplay = False 

# custom hints
c.hints.chars = 'htnsueoai'
c.hints.find_implementation = 'javascript'

# fonts
c.fonts.default_family = "Misc Tamsyn"
c.fonts.completion.category = "bold 12pt default_family"
c.fonts.completion.entry = "12pt default_family"
c.fonts.debug_console = "12pt default_family"
c.fonts.downloads = "12pt default_family"
c.fonts.hints = "bold 12pt default_family"
c.fonts.keyhint = "12pt default_family"
c.fonts.messages.error = "12pt default_family"
c.fonts.messages.info = "12pt default_family"
c.fonts.messages.warning = "12pt default_family"
c.fonts.prompts = "12pt default_family"
c.fonts.statusbar = "12pt default_family"

# editor
c.editor.command = ["kitty", "nvim", "{}"]

# binds
config.bind(",v", "hint links spawn mpv {hint-url}")
