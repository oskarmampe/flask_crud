from flask import Flask
from flask_restful import Resource, Api
import redis
import os
import socket


app = Flask(__name__)
api = Api(app)
cache = redis.Redis(host='redis', port=6379)


class HelloWorld(Resource):
    def get(self):
        return {'hello': 'wor'}


api.add_resource(HelloWorld, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
