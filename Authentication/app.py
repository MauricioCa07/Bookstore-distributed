from flask import Flask, render_template
from extensions import db, login_manager
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bookstore.db'

db.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'auth.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Luego importar blueprints
from controllers.auth_controller import auth
from controllers.admin_controller import admin

# Registrar blueprints
app.register_blueprint(auth)
app.register_blueprint(admin)


@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
