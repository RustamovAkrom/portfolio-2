from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from app.config import config


db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
admin = Admin()

admin.template_mode = "bootstrap4"


def create_app(config_class: str = "app.config.config") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    admin.init_app(app)

    login_manager.login_view = "routes.login"


    from app import models, routes

    app.register_blueprint(routes.main)

    if config.DEBUG:
        admin.add_view(ModelView(models.About, db.session))
        admin.add_view(ModelView(models.Social, db.session))
        admin.add_view(ModelView(models.Service, db.session))
        admin.add_view(ModelView(models.Skill, db.session))
        admin.add_view(ModelView(models.Resume, db.session))
        admin.add_view(ModelView(models.Project, db.session))
        admin.add_view(ModelView(models.Contact, db.session))
        
    return app
