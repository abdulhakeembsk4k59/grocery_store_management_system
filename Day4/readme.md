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


## UOM Handling 
1. create a file name `uom_dao` and add below code in it :- 
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
2. in `server.py` add uom rout :
#### first import `uom_dao.py` in `server.py` then add this rout :
```
