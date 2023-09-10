# import json
# from django.core.management.base import BaseCommand
# # Import your StockData model from the 'sql' app
# from sql.models import StockData


# class Command(BaseCommand):
#     help = 'Load data from a JSON file into the database'

#     def add_arguments(self, parser):
#         parser.add_argument('json_file', type=str,
#                             help='Path to the JSON file')

#     def handle(self, *args, **kwargs):
#         json_file = kwargs['json_file']

#         # Construct the full path to the JSON file
#         file_path = f'./data/{json_file}'

#         # Open and read the JSON file
#         with open(file_path, 'r') as file:
#             data = json.load(file)

#         # Load data into the database using the StockData model
#         for item in data:
#             stock_data = StockData(
#                 date=item['date'],
#                 trade_code=item['trade_code'],
#                 high=item['high'],
#                 low=item['low'],
#                 open=item['open'],
#                 close=item['close'],
#                 volume=item['volume']
#             )
#             stock_data.save()

#         self.stdout.write(self.style.SUCCESS('Data loaded successfully'))

# api/management/commands/load_data.py
import json
from django.core.management.base import BaseCommand
from sql.models import StockData
from django.db import connection


class Command(BaseCommand):
    help = 'Load data into the StockData table'

    def handle(self, *args, **kwargs):
        # Check if the table exists in the database
        table_name = StockData._meta.db_table
        with connection.cursor() as cursor:
            table_exists_query = f"SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = %s);"
            cursor.execute(table_exists_query, [table_name])
            table_exists = cursor.fetchone()[0]

        if table_exists:
            # If the table exists, you can truncate it or delete its contents
            # For example, to truncate the table:
            # StockData.objects.all().delete()

            # To delete all rows but keep the table structure:
            StockData.objects.all().delete()

        with open('./data/stock_data.json', 'r') as json_file:
            data = json.load(json_file)
            for item in data:
                StockData.objects.create(
                    date=item['date'],
                    trade_code=item['trade_code'],
                    high=item['high'],
                    low=item['low'],
                    open=item['open'],
                    close=item['close'],
                    volume=item['volume']
                )
