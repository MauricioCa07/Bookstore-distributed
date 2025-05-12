from flask import Flask
from extensions import login_manager
from models.user import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secretkey'


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


from controllers.purchase_controller import purchase
from controllers.payment_controller import payment
from controllers.delivery_controller import delivery

app.register_blueprint(purchase)
app.register_blueprint(payment)
app.register_blueprint(delivery)


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
