from django.db import models

# Create your models here.


class Categories (models.TextChoices):
    CLOTHING = 'clothing'
    FOOD = 'Food'
    TOOLS = 'Tools'
    TOYS = 'Toys'
    WEAPONS = 'Weapons'

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)
    category = models.CharField(max_length=200, default='none', choices=Categories.choices)
    image = models.ImageField(null=True, blank=True, default='/no_image.png')
    archived = models.BooleanField(default=False)

    def __str__(self):
        return f'name - {self.name} //// price - {self.price} //// category - {self.category} //// image - {self.image} '


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)
    archived = models.BooleanField(default=False)


    def __str__(self):
        return f'product - {self.product.name} //// quantity - {self.quantity}'


    # isActiveCart = True
    # order_id = models.ForeignKey(OrderItem)

# class OrderItem(models.Model):
#     product = models.ForeignKey(Product)
#     quantiy = models.IntegerField()




# class Order
# DateField
# OrderID

# user order productid quantity
# 1     1       2         2
# 1  3   1
# 1  4   1




