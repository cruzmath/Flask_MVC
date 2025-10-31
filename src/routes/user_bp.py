from controllers.user_controller import UserController
from flask import Blueprint

user_blueprint = Blueprint('user', __name__)

user_blueprint.route('/login', methods=['GET', 'POST'])(UserController.login)
user_blueprint.route('/register', methods=['GET', 'POST'])(UserController.register)
user_blueprint.route('/home', methods=['GET'])(UserController.home)
user_blueprint.route('/logout', methods=['GET'])(UserController.logout)
