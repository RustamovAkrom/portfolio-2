from flask import redirect, url_for, request
from flask_admin import AdminIndexView, expose
from flask_admin.contrib.sqla import ModelView
from flask_admin.form import FileUploadField
from flask_login import current_user

from app.config import config


class BaseAdminModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login", next=request.url))


class MyAdminIndexView(AdminIndexView):
    """
    Admin home page
    """

    @expose("/")
    def index(self):
        return self.render("admin/index.html")

    def is_accessible(self):
        return current_user.is_authenticated and current_user.is_admin

    def inaccessible_callback(self, name, **kwargs):
        return redirect(url_for("auth.login", next=request.url))


class AboutView(BaseAdminModelView):
    form_extra_fields = {
        "avatar": FileUploadField("Avatar", base_path=config.UPLOAD_FOLDER)
    }


class ResumeView(BaseAdminModelView):
    form_extra_fields = {
        "file": FileUploadField("Resume", base_path=config.UPLOAD_FOLDER)
    }


class ProjectView(BaseAdminModelView):
    form_extra_fields = {
        "img": FileUploadField("Image", base_path=config.UPLOAD_FOLDER)
    }
    form_columns = ["name", "img", "description", "created", "url", "category"]


class CategoryView(BaseAdminModelView):
    pass


class SocialView(BaseAdminModelView):
    pass


class ServiceView(BaseAdminModelView):
    pass


class SkillView(BaseAdminModelView):
    pass


class ContactView(BaseAdminModelView):
    pass


class UserView(BaseAdminModelView):
    pass
