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
