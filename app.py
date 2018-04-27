from flask import Flask, request, render_template
from flask_restful import Api, reqparse
from flask_jwt import JWT

from security import authenticate, identity
from user import UserRegister
from item import Item, ItemList

app = Flask(__name__)
app.secret_key = 'this is a secret'

api = Api(app)
items = []
jwt = JWT(app, authenticate, identity) # /auth 

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, '/items')
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug=True)
