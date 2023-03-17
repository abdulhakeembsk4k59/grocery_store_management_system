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
