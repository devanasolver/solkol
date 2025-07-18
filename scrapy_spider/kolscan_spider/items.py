import scrapy

class TraderItem(scrapy.Item):
    rank = scrapy.Field()
    display_name = scrapy.Field()
    wallet_id = scrapy.Field()
    trades = scrapy.Field()
    realized_pnl_sol = scrapy.Field()
    realized_pnl_usd = scrapy.Field()
    wallet_link = scrapy.Field()  # For frontend-friendly wallet link
