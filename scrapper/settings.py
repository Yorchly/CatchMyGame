# https://developers.whatismybrowser.com/useragents/explore/software_type_specific/web-browser/1
import os

USER_AGENTS = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36",
    "Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/605.1.15 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:85.0) Gecko/20100101 Firefox/85.0"
)

DELAYS = (2, 3, 4)

REFERER = "https://www.google.es"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

HTML_DIR = os.path.join(BASE_DIR, "html")

ENEBA_FILENAME = "eneba_search.html"

STEAM_FILENAME = "steam_search.html"

INSTANTGAMING_FILENAME = "instantgaming_search.html"
