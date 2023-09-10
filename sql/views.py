from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from .models import StockData
from .serializers import StockDataSerializer
from django.core.paginator import Paginator, EmptyPage
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.middleware import csrf


def get_csrf_token(request):
    csrf_token = csrf.get_token(request)
    return JsonResponse({'csrfToken': csrf_token})


def get_all_data(request):
    data = StockData.objects.all()
    serialized_data = [{
        "id": item.id,
        "date": item.date,
        "trade_code": item.trade_code,
        "high": item.high,
        "low": item.low,
        "open": item.open,
        "close": item.close,
        "volume": item.volume,
    } for item in data]

    response_data = {
        "data": serialized_data,
    }

    return JsonResponse(response_data)


def get_data(request):

    page_number = request.GET.get('page', 1)
    limit = request.GET.get('limit', 10)

    # Convert the page and limit to integers
    try:
        page_number = int(page_number)
        limit = int(limit)
    except ValueError:
        page_number = 1
        limit = 10

    start_limit = page_number * limit - limit
    end_limit = page_number * limit

    data = StockData.objects.all()[start_limit: end_limit]
    trade_codes = list(
        set([entry.trade_code for entry in StockData.objects.all()]))

    # paginator = Paginator(data, limit)

    serialized_data = [{
        "id": item.id,
        "date": item.date,
        "trade_code": item.trade_code,
        "high": item.high,
        "low": item.low,
        "open": item.open,
        "close": item.close,
        "volume": item.volume,
    } for item in data]

    total_length = StockData.objects.count()
    csrf_token = csrf.get_token(request)

    response_data = {
        "data": serialized_data,
        "total_length": total_length,
        'trade_codes': trade_codes,
        'csrf_token': csrf_token,
        "page_number": page_number,
        "limit": limit,
        "start_limit": start_limit,
        "end_limit": end_limit
    }

    return JsonResponse(response_data)


@api_view(['POST'])
def update_data(request):
    try:
        stock_data = StockData.objects.get(pk=request.data.get('id'))
    except StockData.DoesNotExist:
        return Response({"error": "Stock data with this ID does not exist"}, status=status.HTTP_404_NOT_FOUND)

    serializer = StockDataSerializer(stock_data, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


def delete_row(request, row_id):
    try:
        stock_data = get_object_or_404(StockData, id=row_id)
        stock_data.delete()

        return JsonResponse({"message": "Row deleted successfully"}, status=200)
    except Exception as e:
        return JsonResponse({"message": f"Error deleting row: {str(e)}"}, status=500)
