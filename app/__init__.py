from flask import Flask

from app.config import config
from app.extensions import db, migrate, login_manager, mail
from app.admin.admin_setup import setup_admin
from app.context_processor import setup_context_processor
from app.commands import create_admin


def create_app(config_path: str = "app.config.config") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_path)

    # Регистрация команды в CLI
    app.cli.add_command(create_admin)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    login_manager.login_view = "routes.auth.login"
    mail.init_app(app)

    # Конфигурация админ-панели
    setup_admin(app)

    # Настройка глобальных функций
    setup_context_processor(app)

    # Регистрация Blueprint'ов
    from app import routes

    app.register_blueprint(routes.auth_dp)
    app.register_blueprint(routes.site_dp)

    return app
