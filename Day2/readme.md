# Grocery Store Management System | Day 3

## Joining uom_name column from uom table with product table details
Note :- Here i'm doing this because i want to show each products unit name along with it's remaining details. if it is a rice then we have to show it's unit_name as `kg`,
if it is milk then `lt`, and if it is tooth paste then `each` like that...
### forexample you can observ in this image :
<img src="https://i.ibb.co/YXTxtVV/image.png"/>

### query to achieve this :

```
SELECT  products.product_id, products.product_name,
products.uom_id, products.price_per_unit, uom.uom_name 
FROM products inner join uom on products.uom_id=uom.uom_id;
```

### now copy this query to our python code, replace their query with our new query :

<img src="https://i.ibb.co/D8dRjC5/image.png"/>

### and run the program then you can able to see requested results as : 
<img src="https://i.ibb.co/1Ly79wX/image.png"/>


### Lets make our code little bit modular
1.lets create `get_all_products()` method and move whole code into it

2. now call it like this :
```
if __name__=='__main__':
    print(get_all_products())



   
 
inserting products into grocery_store (gs) database