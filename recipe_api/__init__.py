from flask import Flask 
from config import Config 
app = Flask(__name__)
from .authentication.routes import auth
from .site.routes import site

app.config.from_object(Config)


app.register_blueprint(auth)
app.register_blueprint(site)