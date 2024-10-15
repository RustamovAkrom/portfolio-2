from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField

from flask_login import current_user

from app.config import config
from app.extensions import db
from app import models


class AuthAdminModel(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user
    

class AboutView(AuthAdminModel):
    form_overrides = {
        'avatar': FileUploadField
    }
    form_args = {
        'avatar': {
            'base_path': config.UPLOAD_FOLDER
        }
    }


class ResumeView(AuthAdminModel):
    form_overrides = {
        'file': FileUploadField
    }
    form_args = {
        'file': {
            'base_path': config.UPLOAD_FOLDER
        }
    }


def setup_admin(app):
    session = db.session

    admin = Admin(app, name="Portfolio Admin", template_mode="bootstrap3")

    if config.DEBUG:
        admin.add_view(AboutView(models.About, session))

        admin.add_view(AuthAdminModel(models.Social, session))
        admin.add_view(AuthAdminModel(models.Service, session))
        admin.add_view(AuthAdminModel(models.Skill, session))
        admin.add_view(ResumeView(models.Resume, session))
        admin.add_view(AuthAdminModel(models.Project, session))
        admin.add_view(AuthAdminModel(models.Contact, session))