from flask import Flask, flash
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager, logout_user

app = Flask(__name__)
app.config['TESTING'] = False
DB_NAME = "database.db"
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

def create_app():
    app.config['SECRET_KEY'] = 'hdasdasdasdzxc'
    db.init_app(app)

    from .blueprint import bp
    app.register_blueprint(bp, url_prefix='/')

    if not path.exists('project/' + DB_NAME):
        from .models import user as us
        from .models import worker as wo
        db.create_all()
        print('Created Database!')

    login_manager = LoginManager()
    login_manager.login_view = 'sign_up'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        from .models import user
        flash("You have to be logged in to access this page.")
        return user.query.get(int(id))
    return app
#Aby sie wylogować należy kliknąć "zalogowano jako"
@app.before_first_request
def init_app():
    logout_user()


