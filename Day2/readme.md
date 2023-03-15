# Grocery Store Management System | Day 2

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

```
import mysql.connector

def get_all_products():

    cnx = mysql.connector.connect(user='root', password='root',
                                host='127.0.0.1',
                                database='gs')

    cursor = cnx.cursor()
    query =  ("SELECT  products.product_id, products.product_name,"
    "products.uom_id, products.price_per_unit, uom.uom_name "
    "FROM products inner join uom on products.uom_id=uom.uom_id;")


    cursor.execute(query)

    response = []

    for(product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id' : product_id,
            'name': name,
            'uom_id':uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })

    cnx.close()
    return response

```

2. now call it like this :

```
if __name__=='__main__':
    print(get_all_products())

```

<img src="https://i.ibb.co/CPLRgWd/image.png"/>

### Output would be like :
<img src="https://i.ibb.co/2PPTPc9/image.png"/>




## lets make this code even more modular :
### lets move our mySQL connection code into saprate file :
1. so create a file named `sql_connection.py` and copy paste below code init :-

```
import mysql.connector

__cnx = None
def get_sql_connection():
    global __cnx
    if __cnx is None:
        cnx = mysql.connector.connect(user = "root", password="root",
                                    host="127.0.0.1",
                                    database="gs")
    return cnx
```

2. and modify our products_dao.py file according to it :-

```
from sql_connection import get_sql_connection


def get_all_products(connection):


    cursor = connection.cursor()

    query =  ("SELECT  products.product_id, products.product_name,"
    "products.uom_id, products.price_per_unit, uom.uom_name "
    "FROM products inner join uom on products.uom_id=uom.uom_id;")


    cursor.execute(query)

    response = []

    for(product_id, name, uom_id, price_per_unit, uom_name) in cursor:
        response.append({
            'product_id' : product_id,
            'name': name,
            'uom_id':uom_id,
            'price_per_unit': price_per_unit,
            'uom_name': uom_name
        })
    return response
if __name__=='__main__':
    connection = get_sql_connection()
    print(get_all_products(connection))

```

### and output would be the same as before 
<img src="https://i.ibb.co/2PPTPc9/image.png"/>


