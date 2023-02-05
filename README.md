# Shopping Cart project using django and react<br>Project includes:

# Front end in React.js:
react front end that will show the following:
- products screen
- cart screen

should contain the following actions:
- Show all products
- Show products in Cart
- Add a product to Cart
- Remove from Cart
- Update quantity in Cart


# Back end (api) in Django
an api written in django using djangorestframework 

the api will include:

## Products
Product will have a name, description price and image
- get products
- add product
- get single product
- delete product
the delete action - should not delete but mark as archived (therefore the get products, search products should bring only product where archived=False)
- update product

## CartItem
Cart item will contain 2 fields:<br>
 1. product as foreign key <br>
 2. quantity

- get CartItems
- get single CartItem
- add CartItem
- Delete CartItem -  also archive instead of delete
- Update CartItem


## optional enhancements :

(5 bonus points for each one - 100 is still the maximum grade)
- add Order model. The user will click "checkout" which should save the order and clear the cart.<br>
I suggest you add this model first in django.<br> 
then think about how to add it in react<br>
- Search products (react+django)
- See order history
- Authentication (react + django) 

## My recommendation:
deploy this project on the web and add it to your resume (we will go over this in class)
