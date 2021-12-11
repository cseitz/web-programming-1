
```python
from bottle import route, run

# websites default to a path of / when nothing else is specified
# this is effectively the root, homepage, or "index" of your website.
@route("/")
def get_index():
    return ("home page!")

# route decorator
# tells bottle where this function is being mounted on
@route("/hello")
@route("/hello/<name>")
def get_hello(name="world"): # route parameter with default value of "world"
    return (f"Hello, {name}!") # send a response back to the client

# Tell it to listen on our machine at port 8068
run(host="localhost", port=8068)
# website online at http://localhost:8060
```