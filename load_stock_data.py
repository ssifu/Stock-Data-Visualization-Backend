import os
import django
import json
from sql.models import StockData

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "StockMarketData.settings")

# Initialize Django
django.setup()

with open('./data/stock_data.json', 'r') as json_file:
    stock_data = json.load(json_file)

for entry in stock_data:
    StockData.objects.create(
        date=entry['date'],
        trade_code=entry['trade_code'],
        high=entry['high'],
        low=entry['low'],
        open=entry['open'],
        close=entry['close'],
        volume=entry['volume']
    )
