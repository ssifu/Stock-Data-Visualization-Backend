# forms.py
from django import forms
from .models import StockData


class StockDataEditForm(forms.ModelForm):
    class Meta:
        model = StockData
        fields = ['id', 'date', 'trade_code',
                  'high', 'low', 'open', 'close', 'volume']
