# Grocery Store Management System | Day 4

## Python Flask Server Implementation 
so the first thing i'm going to do is in my python code i have a `products_dao.py` file, but i don't have a python `flask` server. in any web backend that has to be a server, so in this we are going to use flask as a micro framwork for our web server, there is an another option called `django` in python but since `flask` is very lightweight we'll just use it.
### so lets define a server :
1. in backend folder create a file `server.py` .
2. The basic boiler plate code to run a basic server in flask is this :

```
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/hello')
def hello():
    return "Hello, how are you"

if __name__=="__main__":
    print("Starting python flask server for Grocery Store Management System")
    app.run(port=5000)

```
copy the above code and paste it in your `server.py` file and run it .
### output :
<img src="https://i.ibb.co/VCRjFFr/image.png"/>
open that link in brower then output would be like :
<img src="https://i.ibb.co/Bw2nDFx/image.png"/>

#### now you have to route for `/hello` :
open this link in browser `127.0.0.1:5000/hello`
##### now output would be like :
<img  src="https://i.ibb.co/ZKjCZ0p/image.png"/>


## now i'm going to create a endpoint which can get us all products on our web page :

it means when i request for `127.0.0.1:5000/getProducts` then it should retrun all the products availeble in our database.

#### in database i have these many products :
<img src="https://i.ibb.co/QQfByB7/image.png"/>
so i have to show these on our web page.

#### so i write a route called `/getProducts` :

```
from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import mysql.connector
import json

import products_dao

app = Flask(__name__)

connection = get_sql_connection()

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5001) # if you get internal server error then you can change port number hrere
    

```
#### follow this article to read about Access-Control-Allow-Origin : <a href="https://developer.mozilla.org/en-US/docs/web/http/headers/access-control-allow-origin">Click Here</a>

#### now output would be like : 
<img src="https://i.ibb.co/m4KgnPH/image.png"/>


### route to delete prodocut :

```
@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
```


### like wise make for route to insert_prodocts , insert_orders etc..; and finally our server.py would be like :

```
from flask import Flask, request, jsonify
from sql_connection import get_sql_connection
import uom_dao
import mysql.connector
import json

import products_dao
import orders_dao


app = Flask(__name__)

connection = get_sql_connection()


@app.route('/getUOM', methods=['GET'])
def get_uom():
    response = uom_dao.get_uoms(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getProducts', methods=['GET'])
def get_products():
    response = products_dao.get_all_products(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/insertProduct', methods=['POST'])
def insert_product():
    request_payload = json.loads(request.form['data'])
    product_id = products_dao.insert_new_product(connection, request_payload)
    response = jsonify({
        'product_id': product_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/getAllOrders', methods=['GET'])
def get_all_orders():
    response = orders_dao.get_all_orders(connection)
    response = jsonify(response)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/insertOrder', methods=['POST'])
def insert_order():
    request_payload = json.loads(request.form['data'])
    order_id = orders_dao.insert_order(connection, request_payload)
    response = jsonify({
        'order_id': order_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route('/deleteProduct', methods=['POST'])
def delete_product():
    return_id = products_dao.delete_product(connection, request.form['product_id'])
    response = jsonify({
        'product_id': return_id
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response



if __name__ == "__main__":
    print("Starting Python Flask Server For Grocery Store Management System")
    app.run(port=5002) # if you get internal server error then you can change port number hrere

```
Note : we're importing `uom_dao` and `orders_dao` because we're implemented those in saprate files .

### uom_dao.py file Code :
```
def get_uoms(connection):
    cursor = connection.cursor()
    query = ("SELECT * from uom")
    cursor.execute(query)

    response = []
    for(uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response

if __name__== '__main__':
    from sql_connection import get_sql_connection

    connection = get_sql_connection()
    print(get_uoms(connection))

```


### orders_dao.py file code :
```
from datetime import datetime
from sql_connection import get_sql_connection

def insert_order(connection, order):
    cursor = connection.cursor()

    order_query = ("INSERT INTO orders "
             "(customer_name, total, datetime)"
             "VALUES (%s, %s, %s)")
    order_data = (order['customer_name'], order['grand_total'], datetime.now())

    cursor.execute(order_query, order_data)
    order_id = cursor.lastrowid

    order_details_query = ("INSERT INTO order_details "
                           "(order_id, product_id, quantity, total_price)"
                           "VALUES (%s, %s, %s, %s)")

    order_details_data = []
    for order_detail_record in order['order_details']:
        order_details_data.append([
            order_id,
            int(order_detail_record['product_id']),
            float(order_detail_record['quantity']),
            float(order_detail_record['total_price'])
        ])
    cursor.executemany(order_details_query, order_details_data)

    connection.commit()

    return order_id

def get_order_details(connection, order_id):
    cursor = connection.cursor()

    query = "SELECT * from order_details where order_id = %s"

    query = "SELECT order_details.order_id, order_details.quantity, order_details.total_price, "\
            "products.product_name, products.price_per_unit FROM order_details LEFT JOIN products on " \
            "order_details.product_id = products.product_id where order_details.order_id = %s"

    data = (order_id, )

    cursor.execute(query, data)

    records = []
    for (order_id, quantity, total_price, product_name, price_per_unit) in cursor:
        records.append({
            'order_id': order_id,
            'quantity': quantity,
            'total_price': total_price,
            'product_name': product_name,
            'price_per_unit': price_per_unit
        })

    cursor.close()

    return records

def get_all_orders(connection):
    cursor = connection.cursor()
    query = ("SELECT * FROM orders")
    cursor.execute(query)
    response = []
    for (order_id, customer_name, total, dt) in cursor:
        response.append({
            'order_id': order_id,
            'customer_name': customer_name,
            'total': total,
            'datetime': dt,
        })

    cursor.close()

    # append order details in each order
    for record in response:
        record['order_details'] = get_order_details(connection, record['order_id'])

    return response

if __name__ == '__main__':
    connection = get_sql_connection()
    print(get_all_orders(connection))
    # print(get_order_details(connection,4))
    # print(insert_order(connection, {
    #     'customer_name': 'dhaval',
    #     'total': '500',
    #     'datetime': datetime.now(),
    #     'order_details': [
    #         {
    #             'product_id': 1,
    #             'quantity': 2,
    #             'total_price': 50
    #         },
    #         {
    #             'product_id': 3,
    #             'quantity': 1,
    #             'total_price': 30
    #         }
    #     ]
    # }))
    ```
