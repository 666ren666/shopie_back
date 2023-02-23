from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product, CartItem
from .serializers import ProductSerializer, CartItemSerializer

# ===================================Products=====================================================

@api_view(['GET', 'POST'])
def products(request):

# List all products that are not archived, or create a new product.
    if request.method == 'GET':
        products = Product.objects.filter(archived=False)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

# create new product
    elif request.method == 'POST': 
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

# Search for products that are not archived.
@api_view(['GET'])
def search_products(request):
    query = request.GET.get('q')
    if query:
        products = Product.objects.filter(Q(name__icontains=query) | Q(description__icontains=query), archived=False)
    else:
        products = Product.objects.filter(archived=False)
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

# show a single product by id 
@api_view(['GET'])
def product(request, pk):
    product = Product.objects.get(id=pk)
    serializer = ProductSerializer(product,many=False)
    return Response(serializer.data)

# delete a single product by id 
@api_view(['DELETE'])
def delete_product(request, pk):
    try: product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    product.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)

# update a single product by id 
@api_view(['PUT'])
def update_product(request, pk):
    try: product = Product.objects.get(id=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ===================================CART-ITEMS====================================================

@api_view(['GET', 'POST'])
def cart_items(request):

# List all cart_items that are not archived, or create a new cart_item.
    if request.method == 'GET':
        cart_items = CartItem.objects.filter(archived=False)
        serializer = CartItemSerializer(cart_items, many=True)
        return Response(serializer.data)

# create new cart_item
    elif request.method == 'POST': 
        serializer = CartItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

# Search for cart_items that are not archived.
@api_view(['GET'])
def search_cart_items(request):
    query = request.GET.get('q')
    if query:
        cart_items = CartItem.objects.filter(Q(name__icontains=query) | Q(description__icontains=query), archived=False)
    else:
        cart_items = CartItem.objects.filter(archived=False)
    serializer = CartItemSerializer(cart_items, many=True)
    return Response(serializer.data)

# show a single cart_item by id 
@api_view(['GET'])
def cart_item(request, pk):
    cart_item = CartItem.objects.get(id=pk)
    serializer = CartItemSerializer(cart_item,many=False)
    return Response(serializer.data)

# delete a single cart_item by id 
# @api_view(['DELETE'])
# def delete_cart_item(request, pk):
#     try: cart_item = CartItem.objects.get(id=pk)
#     except CartItem.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     cart_item.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['DELETE'])
def delete_cart_item(request, pk):
    if request.method == 'DELETE':
        try:
            cart_item = CartItem.objects.get(id=pk)
            cart_item.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except CartItem.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    else:
        return Response(status=status.HTTP_400_BAD_REQUEST)





# update a single cart_item by id 
@api_view(['PUT'])
def update_cart_item(request, pk):
    try: cart_item = CartItem.objects.get(id=pk)
    except CartItem.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = CartItemSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# ===================================PRODUCTS TO CART-ITEMS====================================================

# def add_to_cart(request):
#     if request.method == 'POST':
#         product_id = request.POST.get('product_id')
#         product = Product.objects.get(id=product_id)
#         cart_item = CartItem(product=product)
#         cart_item.save()
#         return JsonResponse({'status': 'success'})
#     else:
#         return JsonResponse({'status': 'error'})




@api_view(['POST'])
def add_to_cart(request):
    product_id = request.data.get('product_id')
    try:
        product = Product.objects.get(id=product_id)
        cart_item = CartItem(product=product)
        cart_item.save()
        return Response({'status': 'success'}, status=status.HTTP_201_CREATED)
    except Product.DoesNotExist:
        return Response({'status': 'error', 'message': 'Product not found.'}, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({'status': 'error', 'message': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
