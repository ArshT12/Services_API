from django.http import JsonResponse
from django.views import View
from .models import Order, OrderItem
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
import json

class OrderList(View):
    def get(self, request):
        orders = Order.objects.all().values()
        return JsonResponse(list(orders), safe=False)

class OrderItemList(View):
    def get(self, request):
        order_items = OrderItem.objects.all().values()
        return JsonResponse(list(order_items), safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class CreateOrder(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            user_id = data.get('user_id')
            total_price = data.get('total_price')

            order = Order.objects.create(
                user_id=user_id,
                total_price=total_price,
                status='pending'
            )

            return JsonResponse({'message': 'Order created successfully!', 'order_id': order.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

@method_decorator(csrf_exempt, name='dispatch')
class CancelOrder(View):
    def post(self, request, order_id):
        try:
            order = Order.objects.get(id=order_id)
            order.status = 'cancelled'
            order.save()

            return JsonResponse({'message': 'Order cancelled successfully!'})
        except Order.DoesNotExist:
            return JsonResponse({'error': 'Order not found.'}, status=404)

