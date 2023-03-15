# Grocery Store Management System | Day 3

## Joining uom_name column from uom table with product table details
Note :- Here i'm doing this because i want to show each products unit name along with it's remaining details. if it is a rice then we have to show it's unit_name as `kg`,
if it is milk then `lt`, and if it is tooth paste then `each` like that...
### forexample you can observ in this image :
<img src="https://i.ibb.co/YXTxtVV/image.png">
### query to achieve this :
```
SELECT  products.product_id, products.product_name,
products.uom_id, products.price_per_unit, uom.uom_name 
FROM products inner join uom on products.uom_id=uom.uom_id;```


inserting products into grocery_store (gs) database
