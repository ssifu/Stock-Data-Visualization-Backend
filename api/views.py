from django.shortcuts import render
from django.http import JsonResponse
import json

# Create your views here.


def get_stock_data(request):
    with open('data/stock_data.json') as json_file:
        data = json.load(json_file)

    return JsonResponse(data, safe=False)
