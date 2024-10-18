from flask_admin import Admin
from app.config import config
from app.extensions import db

from app import models
from .views import MyAdminIndexView, AuthAdminModel, ResumeView, AboutView, ProjectView, CategoryView


def setup_admin(app):
    session = db.session

    admin = Admin(
        app,
        index_view=MyAdminIndexView(),
        name="Portfolio Admin", 
        template_mode="bootstrap3",
    )

    if config.DEBUG:
        admin.add_view(AboutView(models.About, session))

        admin.add_view(AuthAdminModel(models.Social, session))
        admin.add_view(AuthAdminModel(models.Service, session))
        admin.add_view(AuthAdminModel(models.Skill, session))
        admin.add_view(ResumeView(models.Resume, session))
        admin.add_view(ProjectView(models.Project, session))
        admin.add_view(CategoryView(models.Category, session))
        admin.add_view(AuthAdminModel(models.Contact, session))
