
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from order.models import Order
from order.serializers import OrderSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
class CreateOrderView(CreateAPIView):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]


# TODO: Обновление заказа
# TODO: список заказов пользователя

class UserOrdersList(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        user = request.user
        # orders = Order.objects.filter(user=user)
        orders = user.orders.all()
        serializer = OrderSerializer(orders, many=True)
        return Response(orders)





class UpdateOrderStatusView(APIView):
    def patch(self, request, pk):
        status = request.data['status']
        if status not in ['in_process', 'closed']:
            return Response('Неверный статус', status=400)
        order = Order.objects.get(pk=pk)
        order.status = status
        order.save()
        serializer = OrderSerializer(order)
        return Response(serializer.data)