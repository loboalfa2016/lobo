from flask import Flask
from flask_migrate import Migrate
from flask_login import LoginManager
from config import Config
from models import db, Usuario

login_manager = LoginManager()
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    return Usuario.query.get(int(user_id))


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)
    login_manager.init_app(app)

    from routes.auth import auth_bp
    from routes.usuarios import usuarios_bp
    from routes.actividades import actividades_bp
    from routes.entrenamientos import entrenamientos_bp
    from routes.pdf import pdf_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(usuarios_bp)
    app.register_blueprint(actividades_bp)
    app.register_blueprint(entrenamientos_bp)
    app.register_blueprint(pdf_bp)

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
