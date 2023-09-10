from django.urls import path
from . import views

urlpatterns = [
    path("stock-data/", views.get_data, name="stock_data"),
    path("get-csrf-token/", views.get_csrf_token, name="csrf_token"),
    path("all-stock-data/", views.get_all_data, name="all_stock_data"),
    path("update-stock-data/", views.update_data, name="update_stock_data"),
    path("delete-stock-data/<int:row_id>", views.delete_row, name="delete"),
    path("all-stock-data/", views.get_all_data, name="delete"),
]
