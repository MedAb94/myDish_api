from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from .models import Dish
from .serializers import DishSerializer


@api_view(['GET', ])
@permission_classes((AllowAny,))
def dishes_api(request):
    dishes = Dish.objects.all()
    serializer = DishSerializer(dishes, many=True)
    return Response(serializer.data)
