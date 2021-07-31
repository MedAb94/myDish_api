from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404

from datetime import datetime

from dishes.models import Dish
from .models import Choice
from .serializers import ChoiceSerializer
from dishes.serializers import DishSerializer

from django.contrib import auth
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_200_OK


@csrf_exempt
@api_view(["POST"])
@permission_classes((AllowAny,))
def login(request):
    username = request.data.get("username")
    password = request.data.get("password")
    if username is None or password is None:
        return Response({'error': 'Please provide both username and password'},
                        status=HTTP_400_BAD_REQUEST)
    user = auth.authenticate(username=username, password=password)
    if not user:
        return Response({'error': 'Invalid Credentials'},
                        status=HTTP_404_NOT_FOUND)
    token, _ = Token.objects.get_or_create(user=user)
    auth.login(request, user)
    data = {
        'user': {
            'id': user.id,
            'name': user.first_name,
        },
        'token': token.key
    }
    return Response(data, status=HTTP_200_OK)


@api_view(['GET', ])
@permission_classes((AllowAny,))
def get_choices(request):
    choices = Choice.objects.all()
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes((AllowAny,))
def get_user_choices(request, user_id):
    user = User.objects.get(pk=user_id)
    choices = Choice.objects.filter(user=user)
    serializer = ChoiceSerializer(choices, many=True)
    return Response(serializer.data)


@api_view(['GET', ])
@permission_classes((AllowAny,))
def get_day_order(request):
    today = datetime.today()
    choices = Choice.objects.filter(date__contains=today.strftime('%Y-%m-%d'))
    serializer = ChoiceSerializer(choices, many=True)
    serializer1 = DishSerializer(choices, many=True)
    dishes_ids = []
    dishes_unique_ids = []
    for c in choices:
        dishes_ids.append(c.dish_id)

    for c in choices:
        if c.dish_id not in dishes_unique_ids:
            dishes_unique_ids.append(c.dish_id)

    dishes = Dish.objects.filter(pk__in=dishes_unique_ids)
    return Response(dishes_ids)


@api_view(['POST', ])
@permission_classes((AllowAny,))
def create_choice(request, uid, did):
    user_id = uid
    dish_id = did

    user = get_object_or_404(User, pk=user_id)
    dish = get_object_or_404(Dish, pk=dish_id)
    Choice.objects.create(user=user, dish=dish)
    return Response({"Response": "Choice created successfully"})
