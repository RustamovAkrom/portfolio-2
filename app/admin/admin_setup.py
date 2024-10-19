from flask_admin import Admin
from app.config import config
from app.extensions import db

from app import models
from .views import (
    MyAdminIndexView, 
    ResumeView, 
    AboutView, 
    ProjectView, 
    CategoryView, 
    SocialView, 
    ServiceView, 
    SkillView, 
    ContactView,
    UserView
)


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
        admin.add_view(SocialView(models.Social, session))
        admin.add_view(ServiceView(models.Service, session))
        admin.add_view(SkillView(models.Skill, session))
        admin.add_view(ResumeView(models.Resume, session))
        admin.add_view(ProjectView(models.Project, session))
        admin.add_view(CategoryView(models.Category, session))
        admin.add_view(ContactView(models.Contact, session))
        admin.add_view(UserView(models.User, session))
