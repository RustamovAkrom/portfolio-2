from flask import Flask
from flask_admin.contrib.sqla import ModelView

from app.config import config
from app.extensions import db, migrate, login_manager
from app.admin.views import setup_admin


def create_app(config_class: str = "app.config.config"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "routes.auth.login"

    # configure admin panel
    setup_admin(app)

    from app import routes

    app.register_blueprint(routes.auth_dp)
    app.register_blueprint(routes.site_dp)
        
    return app
