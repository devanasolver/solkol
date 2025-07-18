# Kolscan Leaderboard Scraper and API

This project scrapes the Realized PnL Leaderboard from [kolscan.io](https://kolscan.io/leaderboard) using Scrapy and serves the scraped data via a RESTful API built with Flask.

## Project Structure

- `scrapy_spider/`: Scrapy project to scrape the leaderboard.
- `data/data.json`: JSON file where scraped data is saved.
- `api.py`: Flask API serving the scraped data.
- `refresh_data.sh`: Script to run the spider for refreshing data.
- `requirements.txt`: Python dependencies.

## Setup Instructions

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the Scrapy Spider

Navigate to the `scrapy_spider` directory and run the spider:

```bash
cd scrapy_spider
scrapy crawl leaderboard
```

This will scrape the leaderboard and save the data to `../data/data.json`.

### 3. Run the Flask API

From the project root, run:

```bash
python api.py
```

The API will be available at `http://127.0.0.1:5000/leaderboard`.

### 4. Auto-refresh Data (Optional)

You can set up a cron job or scheduled task to run the `refresh_data.sh` script daily to keep the data updated.

Example cron entry (runs at midnight daily):

```cron
0 0 * * * /bin/bash /path/to/kolscan_leaderboard_api/refresh_data.sh
```

## Notes

- The API endpoint `/leaderboard` returns the latest scraped data as JSON.
- Wallet IDs are linked to [solscan.io](https://solscan.io/address/) for frontend-friendly access.
- The scraper handles missing or zero values gracefully.

## License

This project is open-source and free to use.
