from flask import Flask, render_template
from extensions import db, login_manager
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from controllers.book_controller import book
app.register_blueprint(book, url_prefix='/book')



if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
