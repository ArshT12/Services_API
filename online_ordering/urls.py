from django.urls import path
from .views import OrderList, OrderItemList, CreateOrder, CancelOrder

urlpatterns = [
    path('orders/', OrderList.as_view(), name='order-list'),
    path('order_items/', OrderItemList.as_view(), name='order-item-list'),
    path('orders/create/', CreateOrder.as_view(), name='create-order'),
    path('orders/cancel/<int:order_id>/', CancelOrder.as_view(), name='cancel-order'),
]

