from flask import Flask 
from config import Config 
app = Flask(__name__)
from .authentication.routes import auth
from .site.routes import site
from .models import db, User
from flask_migrate import Migrate
app.config.from_object(Config)



db.init_app(app)
migrate = Migrate(app, db)
app.register_blueprint(auth)
app.register_blueprint(site)