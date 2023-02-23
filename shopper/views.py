from django.contrib.auth import authenticate, login
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import ShopperSerializer
from shopper.models import Shopper
from django.http import JsonResponse


@api_view(['GET', 'POST'])
def shoppers(request):
    """
    List all shoppers, or create a new shopper.
    """
    if request.method == 'GET': # list shoppers
        shoppers = Shopper.objects.all()
        serializer = ShopperSerializer(shoppers, many=True)
        return Response(serializer.data)

    elif request.method == 'POST': # create new shopper
        serializer = ShopperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['POST'])
@csrf_exempt
def create_new_shopper(request):
        serializer = ShopperSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def login_shopper(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        shopper = authenticate(request, email=email, password=password)
        if shopper is not None:
            login (request, shopper)
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'message': 'Invalid email or password'})
    else:
        return JsonResponse({'success': False, 'message': 'Invalid request method'})


@api_view(['GET', 'POST'])
def logout_shopper (self, request, format=None):
    logout_shopper(request)
    response = Response(None, status=status.HTTP_204_NO_CONTENT)
    response.set_cookie('sessionid',max_age=1,samesite='None')
    response.set_cookie('csrftoken',max_age=1,samesite='None')
    return response
    # permission_classes = (permissions.AllowAny,)