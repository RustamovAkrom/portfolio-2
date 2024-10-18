from flask import Flask

from app.extensions import db, migrate, login_manager
from app.admin import setup_admin
from app.context_processor import setup_context_processor


def create_app(config_class: str = "app.config.config"):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "routes.auth.login"

    # configure admin panel
    setup_admin(app)

    # configure global functions
    setup_context_processor(app)

    from app import routes

    app.register_blueprint(routes.auth_dp)
    app.register_blueprint(routes.site_dp)
        
    return app
