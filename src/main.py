from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from routes.user_bp import user_blueprint
from models.user import db
    
app = Flask(__name__, template_folder='views')
app.config.from_object(Config)
app.secret_key = app.config.get('SECRET_KEY')
app.register_blueprint(user_blueprint)

db.init_app(app)
with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True)
