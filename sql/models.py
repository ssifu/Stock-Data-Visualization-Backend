from django.db import models


class StockData(models.Model):
    id = models.BigAutoField(primary_key=20)
    date = models.DateField()
    trade_code = models.CharField(max_length=255)
    high = models.CharField(max_length=10)
    low = models.CharField(max_length=10)
    open = models.CharField(max_length=10)
    close = models.CharField(max_length=10)
    volume = models.CharField(max_length=20)

    def __str__(self):
        return self.trade_code
