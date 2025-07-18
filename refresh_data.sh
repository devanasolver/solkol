#!/bin/bash
# Script to run the Scrapy spider to refresh data

cd "$(dirname "$0")/scrapy_spider"
scrapy crawl leaderboard
