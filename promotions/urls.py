from django.urls import path
from .views import promotion_list_view, product_detail_view

urlpatterns = [
    path('', promotion_list_view),
    path("product-detail/<int:prod_id>", product_detail_view)
]