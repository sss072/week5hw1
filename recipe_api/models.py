from flask_sqlalchemy import SQLAlchemy 
import uuid
import secrets
import datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash


login_manager = LoginManager()



db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String, primary_key = True, unique = True)
    email = db.Column(db.String(150), unique= True, nullable=False)
    password = email = db.Column(db.String, nullable = False)
    token = db.Column(db.String, nullable = False)
    date_created = db.Column(db.DateTime, default = date.utcnow)
    
    def __init__(self, email, password, token = '', id = ''):
        self.id = self.set_id()
        self.email = email
        self.password = self.set_password(password)
        self.token = self.get_token(24)

        def set_id(self):
            return str(uuid.uuid4())

        def set_password(self, password):
            self.pw_hash = generate_password_hash(password)
            return self.pw_hash   

        def get_token(self,length):
            return secrets.token(length)