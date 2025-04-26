from flask import Flask, request, jsonify, make_response
from flask_restful import Api, Resource
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt_identity
from flask_cors import CORS, cross_origin
from flask_bcrypt import Bcrypt
from models import db, Docs, Client, Program
import os

app = Flask(__name__)

# Configuration
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///healthwise.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JWT_SECRET_KEY'] = os.urandom(32).hex()
app.json.compact = False

# Extensions
migrate = Migrate(app, db)
db.init_app(app)
api = Api(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)
CORS(app)

# Index route
class IndexPage(Resource):
    @cross_origin()
    def get(self):
        return {"message": "Welcome to healthwise HMS API"}

api.add_resource(IndexPage, '/')

# Signup route
class DocSignup(Resource):
    @cross_origin()
    def post(self):
        new_user = Docs(
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

        access_token = create_access_token(identity=new_user.email)
        user_dict = new_user.to_dict()
        user_dict['access_token'] = access_token

        return make_response(user_dict, 201)

# Login route
class DocLogin(Resource):
    @cross_origin()
    def post(self):
        email = request.json['email']
        password = request.json['password']
        

        doctor = Docs.query.filter_by(email=email).first()

        if doctor is None:
            return jsonify({'error': 'Unauthorized user!'}), 401
        if not bcrypt.check_password_hash(doctor.password, password):
            return jsonify({"error": "Invalid password"}), 401

        access_token = create_access_token(identity=doctor.email)

        return make_response(jsonify(
            email=doctor.email,
            username=doctor.username,
            department=doctor.department,
            description=doctor.description,
            phone_number=doctor.phone_number,
            profile_picture=doctor.profile_picture,
            access_token=access_token
        ), 200)

# Client Signup route
class ClientSignup(Resource):
    # @jwt_required()
    def post(self):
        new_user = Client(
            username=request.json['username'],
            email=request.json['email'],
            phone_number=request.json['phone_number'],
            gender=request.json['gender'],
            age=request.json['age'],
            date_of_birth=request.json['date_of_birth'],
            address=request.json['address'],
            occupation=request.json['occupation'],
            emergency_contact=request.json['emergency_contact'],
            primary_care_provider=request.json['primary_care_provider'],
            insurance_provider=request.json['insurance_provider'],
            insurance_policy_number=request.json['insurance_policy_number'],
            allergies=request.json['allergies'],
            current_medications=request.json['current_medications'],
            medical_history=request.json['medical_history'],
            family_medical_history=request.json['family_medical_history'],
        )

        db.session.add(new_user)
        db.session.commit()

        new_user_dict = new_user.to_dict()
        response = make_response(new_user_dict, 201)
        return response

# Client Search route
class ClientSearch(Resource):
    # @jwt_required()
    def get(self, query):
        # Find all clients whose usernames start with the query
        clients = Client.query.filter(Client.username.ilike(f"{query}%")).all()

        if clients:
            return make_response([client.to_dict() for client in clients], 200)
        else:
            return {'message': 'No clients found'}, 404
        
#create a program
class Programs(Resource):
    @jwt_required()
    def post(self):
        new_program = Program(
            name=request.json['name'],
            description=request.json['description'],
            slogan=request.json['slogan'],
            program_manager=request.json['program_manager'],
        )
        db.session.add(new_program)
        db.session.commit()
        
        new_program_dict = new_program.to_dict()
        response = make_response(new_program_dict, 201)
        return response
    
#Expose client profile api
class ClientProfile(Resource):
    # @jwt_required()

    def get(self, email):
        client=Client.query.filter_by(email=email).first()
        if client:
            return make_response(client.to_dict(), 200)
        else:
            return {'message': 'Client not found'}, 404
        
class GetClients(Resource):
    # @jwt_required()
    def get(self):
        clients = Client.query.all()
        return make_response([client.to_dict() for client in clients], 200)
    
        
    
        
# Register the resources
api.add_resource(DocSignup, '/doc_signup')
api.add_resource(DocLogin, '/doc_login')
api.add_resource(ClientSignup, '/client_signup')
api.add_resource(ClientSearch, '/client_search/<string:query>')
api.add_resource(Programs, '/program')
api.add_resource(ClientProfile, '/client_profile/<string:email>')
api.add_resource(GetClients, '/clients')



        

# Run the server
if __name__ == '__main__':
    app.run(port=5555, debug=True)
