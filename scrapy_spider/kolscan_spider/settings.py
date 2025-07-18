BOT_NAME = 'kolscan_spider'

SPIDER_MODULES = ['kolscan_spider.spiders']
NEWSPIDER_MODULE = 'kolscan_spider.spiders'

ROBOTSTXT_OBEY = True

FEEDS = {
    '../data/data.json': {
        'format': 'json',
        'encoding': 'utf8',
        'indent': 4,
        'overwrite': True,
    }
}

# Configure a delay for requests to the same website
DOWNLOAD_DELAY = 1

# Disable cookies (enabled by default)
COOKIES_ENABLED = False

# Override the default request headers:
DEFAULT_REQUEST_HEADERS = {
   'User-Agent': 'kolscan_leaderboard_scraper (+http://www.insiderwallets.com)'
}
