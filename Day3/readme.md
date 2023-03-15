# Grocery Store Management System | Day 3


# inserting products into grocery_store (gs) database through python code

in mySql we use `insert into` command to insert value to our db table
### consider this Query as a example for inserting values into products table in our gs database :

```
insert into products (name, uom_id, price_per_unit)
values('sprite', '3', '49');

```

#### Output would be like : 
<img src="https://i.ibb.co/10jDdsB/image.png"/>

## lets do the same task using pyhton code :

### insertion python code :
```
def insert_new_product(connection, product):
    cursor = connection.cursor()
    query = ("insert into products" 
             "(product_name, uom_id, price_per_unit)"
             "values(%s, %s, %s);")
    
    data = (product['product_name'], product['uom_id'], product['price_per_unit'])
    cursor.execute(query,data)
    connection.commit()

    return cursor.lastrowid


if __name__=='__main__':
    connection = get_sql_connection()
    print(insert_new_product(connection, {
        'product_name': 'cabage',
        'uom_id':'1',
        'price_per_unit': '10'
    }))

```
### output would be like :
<img src="https://i.ibb.co/ZGxzv4Z/image.png"/>


# Deletion of products from grocery_store (gs) database through python code :

### consider this code example for deletion :
```
# deletion of products
def delete_product(connection, product_id):
    cursor = connection.cursor()
    query = "DELETE FROM products where product_id="+str(product_id)
    cursor.execute(query)
    connection.commit()


if __name__=='__main__':
    connection = get_sql_connection()

    # for deletion :
    #it will return none but element containing product_id 9 would be deleted
    print(delete_product(connection, 9)) 

```

### Output would be like :
<img src="https://i.ibb.co/BCMqh3V/image.png"/>

here you can see product `cabage` which is having product_id `9` has been deleted.

