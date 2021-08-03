#################
#### imports ####
#################
import os
from flask import Flask
#from flask.ext.sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

from flask_mail import Mail

# local imports
from config import app_config



################
#### config ####
################
config_name = os.getenv('FLASK_ENV', 'development')
template_dir = os.path.abspath('src/app/templates')

app = Flask(__name__, instance_relative_config=True, template_folder=template_dir)
app.config.from_object(app_config[config_name])

bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)

###test
login_manager.login_view = 'user.login'

#app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)
ma = Marshmallow(app)

mail = Mail(app)
#login_manager.login_view = "users.login"


#from app.model.user import User
from app.model.usertwo import User


@login_manager.user_loader
def load_user(user_id):
    # sqlalchemy query
    return User.query.filter(User.id == int(user_id)).first()


def create_app():
        
    
    #from app.route.users.views import bpusr
    #from app.route.home.views import bphome
    #app.register_blueprint(bpusr)
    #app.register_blueprint(bphome)

    from app.route.userstwo.views import bpuser2
    app.register_blueprint(bpuser2)


    #from project.users.views import users_blueprint
    #from project.home.views import home_blueprint

    # register our blueprints
    #app.register_blueprint(users_blueprint)
    #app.register_blueprint(home_blueprint)


    #from model.user import User

    
    #app.config.from_pyfile('config.py')
    #db.init_app(app)
    #ma.init_app(app)

    print(template_dir)
    
    return app

#@login_manager.user_loader
#def load_user(user_id):
#    return User.query.filter(User.id == int(user_id)).first()
