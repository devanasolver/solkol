import scrapy
from kolscan_spider.items import TraderItem

class LeaderboardSpider(scrapy.Spider):
    name = "leaderboard"
    allowed_domains = ["kolscan.io"]
    start_urls = ["https://kolscan.io/leaderboard"]

    def parse(self, response):
        rows = response.css('table tbody tr')
        for index, row in enumerate(rows, start=1):
            item = TraderItem()
            item['rank'] = index
            item['display_name'] = row.css('td:nth-child(2) a::text').get(default='').strip()
            item['wallet_id'] = row.css('td:nth-child(2) a::attr(href)').re_first(r'/address/(.+)')
            trades_text = row.css('td:nth-child(3)::text').get(default='').strip()
            item['trades'] = trades_text if trades_text else '0 / 0'
            pnl_sol = row.css('td:nth-child(4)::text').get(default='0').strip()
            item['realized_pnl_sol'] = pnl_sol if pnl_sol else '0'
            pnl_usd = row.css('td:nth-child(5)::text').get(default='0').strip()
            item['realized_pnl_usd'] = pnl_usd if pnl_usd else '0'
            # Frontend-friendly wallet link
            wallet_id = item['wallet_id']
            if wallet_id:
                item['wallet_link'] = f"https://solscan.io/address/{wallet_id}"
            else:
                item['wallet_link'] = ''
            yield item
