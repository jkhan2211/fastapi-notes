from fastapi import FastAPI

app = FastAPI()

# path and query simulataneously 
# /profile/10/comments?commentid=2

@app.get('/profile/{user_id}/comments')
def profile(user_id: int, commentid:int ):
    return {f"Profile page for user {user_id} with limit of comments is {commentid}"}


#Query Parameter
#/products?id=10
#/products?id=10&price=40
@app.get('/products')
def products(id,price):
    return {f"product with an {id} and price is {price}"}


#Required Query Parameter
# By default is required

@app.get('/products')
def products(id:int=None,price:int=None):
    return {f"product with an {id} and price is {price}"}

@app.get('/')
def index():
    return "Hello World"

# @app.get('/property/1')
# def propert():
#     return "This is a property: One"

# @app.get('/property/2')
# def propert():
#     return "This is a property: Two"


@app.get('/property/{id}')
def property(id: int):
    return {f"This is a property page for property {id}"}

#Ordering of the routes matter, if they possibly clash, make sure they are handled in correct order

@app.get('/user/admin')
def user():
    return {"This is the admin panel"}

@app.get('/user/{user_name}')
def user(user_name: str):
    return {f"This is a user page for user {user_name}"}




@app.get('/movies')
def movies():
    return {"movies_list": ["movie1", "movie2", "movie3"]}

