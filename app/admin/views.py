from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField

from app.config import config
from app.extensions import db
from app import models


class AboutView(ModelView):
    form_overrides = {
        'avatar': FileUploadField
    }
    form_args = {
        'avatar': {
            'base_path': config.UPLOAD_FOLDER
        }
    }


class ResumeView(ModelView):
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

        admin.add_view(ModelView(models.Social, session))
        admin.add_view(ModelView(models.Service, session))
        admin.add_view(ModelView(models.Skill, session))
        admin.add_view(ResumeView(models.Resume, session))
        admin.add_view(ModelView(models.Project, session))
        admin.add_view(ModelView(models.Contact, session))