AUTHOR = 'Jan Gebauer'
SITENAME = 'Sunshine Blog'
SITEURL = ""

PATH = "content"

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True


# Other
AUTHOR     = 'Jan Gebauer'
SITENAME   = 'GitHub Page'
SITEURL    = ''           # set to full URL for production

PATH       = 'content'
THEME      = 'theme'      # path to this theme folder

TIMEZONE   = 'Europe/Berlin'
DEFAULT_LANG = 'en'

# Put pages in the nav — no date-based URLs for pages
PAGE_URL      = '{slug}.html'
PAGE_SAVE_AS  = '{slug}.html'


CONTACT_FIELDS = [
    {
        "icon":  "🪪",
        "label": "Name",
        "value": "Jan Gebauer",
        "url":   None,
    },
    {
        "icon":  "🌐",
        "label": "Website",
        "value": "sunshineworks.eu",
        "url":   "https://sunshineworks.eu",
    },
    {
        "icon":  "📬",
        "label": "Email",
        "value": "post@sunshineworks.eu",
        "url":   "mailto:post@sunshineworks.eu",
    },
    {
        "icon":  "▶️",
        "label": "YouTube",
        "value": "Sunshine Works",
        "url":   "https://www.youtube.com/@sunshineworks",
    },
]