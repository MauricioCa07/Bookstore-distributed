from flask import Flask, render_template
from extensions import login_manager,db
from models.user import User
import config 

app = Flask(__name__)
app.config.from_object(config)

db.init_app(app)
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from controllers.book_controller import book
app.register_blueprint(book, url_prefix='/book')


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
