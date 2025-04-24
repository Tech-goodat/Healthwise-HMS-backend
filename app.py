from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource, reqparse
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, jwt_required, get_jwt_identity, create_access_token, unset_jwt_cookies
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from models import db, Docs
import os

app=Flask(__name__)

app.config ['SQLALCHEMY_DATABASE_URI']= 'sqlite:///healthwise.db'
app.config ['SQLALCHEMY_TRACK_MODIFICATIONS']= False
app.config ['JWT_SECRET_KEY']=os.urandom(32).hex()
app.json.compact=False

migrate=Migrate(app, db)

db.init_app(app)
api=Api(app)
jwt=JWTManager(app)
bcrypt=Bcrypt(app)
CORS(app)


class IndexPage(Resource):
    @cross_origin()
    def get(self):
        return{"message":"Welcome to healthwise HMS API"}

api.add_resource(IndexPage, '/')

class DocSignUp(Resource):
    @cross_origin()
    def post(self):
        new_user=Docs(
            username=request.json['username'],
            email=request.json['email'],
            department=request.json['department'],
            description=request.json['description'],
            phone_number=request.json['phone_number'],
            profile_picture=request.json['profile_picture'],
            password=bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
            
        )

        db.session.add(new_user)
        db.session.commit()

        access_token=create_access_token(identity=new_user.email)
        user_dict=new_user.to_dict()
        user_dict['access_token']=access_token

        response=make_response(user_dict, 201)
        return response
    
api.add_resource(DocSignUp, '/doc_signup')



if __name__=='__main__':
    app.run(port=5555, debug=True)