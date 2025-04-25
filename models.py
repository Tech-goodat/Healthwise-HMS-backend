from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates
from sqlalchemy import MetaData

convention ={"ix": "ix_%(column_0_label)s",                   
    "uq": "uq_%(table_name)s_%(column_0_name)s",    
    "ck": "ck_%(table_name)s_%(constraint_name)s",  
    "fk": "fk_%(table_name)s_%(column_0_name)s",    
    "pk": "pk_%(table_name)s" }

metadata=MetaData(naming_convention=convention)
db=SQLAlchemy(metadata=metadata)

class Docs(db.Model, SerializerMixin):
    __tablename__='doctors'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    email=db.Column(db.String)
    department=db.Column(db.String)
    description=db.Column(db.String)
    phone_number=db.Column(db.String)
    profile_picture=db.Column(db.String)
    password=db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default=db.func.now())

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('invail email address')
        return email
    
    def __repr__(self):
        return f'<Docs {self.id}, {self.username}, {self.email}, {self.department}, {self.description}, {self.phone_number}, {self.profile_picture}, {self.password}, {self.created_at}>'
    
class Client(db.Model, SerializerMixin):
    __tablename__='clients'
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String)
    email=db.Column(db.String)
    phone_number=db.Column(db.String)
    age=db.Column(db.Integer)
    gender=db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default=db.func.now())
    date_of_birth=db.Column(db.String)
    address=db.Column(db.String)
    occupation=db.Column(db.String)
    emergency_contact=db.Column(db.String)
    primary_care_provider=db.Column(db.String)
    insurance_provider=db.Column(db.String)
    insurance_policy_number=db.Column(db.String)
    allergies=db.Column(db.String)
    medical_history=db.Column(db.String)
    current_medications=db.Column(db.String)
    family_medical_history=db.Column(db.String)



    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError('invail email address')
        return email
    def __repr__(self):
        return f'<Client {self.id}, {self.username}, {self.email}, {self.phone_number}, {self.age}, {self.gender}, {self.created_at}, {self.date_of_birth}, {self.address}, {self.occupation}, {self.emergency_contact}, {self.primary_care_provider}, {self.insurance_provider}, {self.insurance_policy_number}, {self.allergies}, {self.current_medications}, {self.medical_history}, {self.family_medical_history}>'
    
class Program(db.Model, SerializerMixin):
    __tablename__='programs'
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String, nullable=False, unique=True)
    description=db.Column(db.String)
    slogan=db.Column(db.String)
    program_manager=db.Column(db.String)
    created_at=db.Column(db.DateTime, server_default=db.func.now())

    def repr__(self):
        return f'<Program {self.id}, {self.name}, {self.description}, {self.created_at}>'
    
