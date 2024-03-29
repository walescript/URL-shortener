from datetime import datetime
from .extensions import db, login_manager, bcrypt
import string
from random import choices
from flask_login import UserMixin

class Link(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(512))
    short_url = db.Column(db.String(4), unique=True)
    custom_url = db.Column(db.String(50), unique=True)
    visits = db.Column(db.Integer, default=0)
    date_created = db.Column(db.DateTime(), default=datetime.now)
    qr_code_url = db.Column(db.String(512))    # New field for storing QR code image URL
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if not self.custom_url:
            self.short_url = self.generate_short_link()

    def save(self):
        db.session.add(self)
        db.session.commit()

    # Generate the short link
    def generate_short_link(self):
        chars = string.ascii_letters + string.digits
        short_url = ''.join(choices(chars, k=4))

        link = self.query.filter_by(short_url=short_url).first()

        if link:
            return self.generate_short_link()
        
        return short_url
    
    # Set the QR code image path
    def set_qr_code_path(self, image_path):
        self.qr_code_url = image_path
        self.save()

    

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), nullable=False)
    email = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(128), nullable=False)
    date_created = db.Column(db.DateTime(), default=datetime.now)
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    links = db.relationship('Link', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def set_password(self, password):
        self.password = self.hash_password(password)
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    def hash_password(self, password):
        return bcrypt.generate_password_hash(password).decode('utf-8')