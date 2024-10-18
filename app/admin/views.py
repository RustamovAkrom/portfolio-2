from flask import redirect, url_for, request
from flask_admin import AdminIndexView
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from flask_login import current_user

from app.config import config


class AuthAdminModel(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))


class MyAdminIndexView(AdminIndexView):
    """
    Admin home page
    """
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin
    
    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for('auth.login', next=request.url))

    
class AboutView(AuthAdminModel):
    form_extra_fields = {
        'avatar': FileUploadField('Avatar', base_path=config.UPLOAD_FOLDER)
    }


class ResumeView(AuthAdminModel):
    form_extra_fields = {
        'file': FileUploadField('Resume', base_path=config.UPLOAD_FOLDER)
    }


class ProjectView(AuthAdminModel):
    form_extra_fields = {
        'img': FileUploadField('Image', base_path=config.UPLOAD_FOLDER)
    }
