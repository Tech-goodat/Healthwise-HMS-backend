from flask import Flask
from flask_restful import Api, Resource

app=Flask(__name__)
api=Api(app)

class IndexPage(Resource):
    def get(self):
        return{"message":"Welcome to healthwise HMS API"}

api.add_resource(IndexPage, '/')

if __name__=='__main__':
    app.run(port=5555, debug=True)