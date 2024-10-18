from datetime import datetime

from flask_login import UserMixin
from app import db


class BaseModel(db.Model):
    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)


class User(BaseModel, UserMixin):
    __tablename__ = "users"

    username = db.Column(db.String(150), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    password = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    def __repr__(self):
        return f"<{self.username}>"
    

class About(BaseModel):
    __tablename__ = "abouts"

    avatar = db.Column(db.String, nullable=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    bio = db.Column(db.String(300), nullable=False)
    phone = db.Column(db.String(16), nullable=False)
    website_url = db.Column(db.String(200), nullable=False)
    city = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False, default=0)
    degree = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(170), nullable=False)
    frelance = db.Column(db.String(100), nullable=True)
    address = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<{self.first_name} {self.last_name}>"
    

class Social(BaseModel):
    __tablename__ = "socials"

    name = db.Column(db.String(100), nullable=False)
    url = db.Column(db.String(200), nullable=False)
    style = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<{self.name}>"
    

class Service(BaseModel):
    __tablename__ = "services"

    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(150), nullable=False)
    url = db.Column(db.String(200), nullable=True)
    style = db.Column(db.String(100), nullable=True)

    def __repr__(self):
        return f"<{self.name}>"
    

class Skill(BaseModel):
    __tablename__ = "skills"

    name = db.Column(db.String(100), nullable=False)
    procent = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<{self.name} - {self.procent}%>"


class Resume(BaseModel):
    __tablename__ = "resumes"
    
    file = db.Column(db.String, nullable=False)
    content = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Resume - {self.id}"


class Category(BaseModel):
    __tablename__ = "categories"

    name = db.Column(db.String(100), nullable=False, unique=True)
    projects = db.relationship('Project', backref='category', lazy=True)

    def __repr__(self):
        return f"<{self.name}>"
    

class Project(BaseModel):
    __tablename__ = "projects"

    name = db.Column(db.String, nullable=False)
    img = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    created = db.Column(db.DateTime, nullable=False)
    url = db.Column(db.String(200), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)

    def __repr__(self):
        return f"<{self.name}>"


class Contact(BaseModel):
    __tablename__ = "contacts"

    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(170), nullable=False)
    subject = db.Column(db.String(100), nullable=False)
    message = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<{self.name} - {self.subject}>"
