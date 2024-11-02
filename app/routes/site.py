import random
import os

from flask import (
    Blueprint,
    render_template,
    abort,
    send_from_directory,
    flash,
    url_for,
    redirect,
    request,
)
from flask_mail import Message
from app.models import Resume, About, Skill, Service, Project, Category, Contact
from app.extensions import db, mail
from app.config import config
from app.utils import htmx_route

import markdown


dp = Blueprint("site", __name__)


@dp.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(config.UPLOAD_FOLDER, filename)


@dp.route("/upload", methods=["POST"])
def uplod_file():
    if "file" not in request.files:
        return "No File part", 400
    file = request.files["file"]
    if file.filename == "":
        return "No selected file", 400
    file.save(os.path.join(config.UPLOAD_FOLDER, file.filename))

    file_url = url_for("site.uploaded_file", filename=file.filename)
    return redirect(file_url)


@dp.route("/")
@dp.route("/home")
@htmx_route()
def index():
    resume_data = Resume.query.first()
    about_data = About.query.first()

    about_avatar_url = None
    if about_data:
        about_avatar_url = about_data.avatar

    context = {
        "template_name": "site/index.html",
        # "template_title": "Rustamov Akrom",
        "template_body_class_name": "index",
        "resume": resume_data,
        "about_avatar_url": about_avatar_url,
        "baground_image": "1.jpg",
    }
    return context


@dp.route("/about")
@htmx_route()
def about():
    about_data = About.query.first()
    skills_data = Skill.query.all()
    skills_count = len(skills_data) // 2
    left_skills = skills_data[:skills_count]
    right_skills = skills_data[skills_count:]

    context = {
        "template_name": "site/about.html",
        "template_title": "About",
        "template_body_class_name": "about",
        "about": about_data,
        "left_skills": left_skills,
        "right_skills": right_skills,
    }
    return context


@dp.route("/contact", methods=["GET", "POST"])
@htmx_route()
def contact():
    about_data = About.query.first()

    if request.method == "POST":
        try:
            name = request.form.get("name", None)
            email = request.form.get("email", None)
            subject = request.form.get("subject", None)
            message = request.form.get("message", None)

            if (name and email and subject and message) is not None:
                contact_data = Contact(
                    name=name, email=email, subject=subject, message=message
                )
                db.session.add(contact_data)
                db.session.commit()

                msg = Message(
                    f"{subject} from {name}",
                    sender=email,
                    recipients=[config.MAIL_USERNAME],
                )
                msg.body = message
                mail.send(msg)
                flash("Successfully send message.", "success")

            else:
                flash("Invalid sending e-mail", "warning")
                print("Invalid fields.")

        except Exception as e:
            flash("Failed to send message. Please try again later.", "danger")
            print("Error", e)

    context = {
        "template_name": "site/contact.html",
        "template_title": "Contacts",
        "template_body_class_name": "contact",
        "about": about_data,
    }

    return context


@dp.route("/portfolio")
@htmx_route()
def portfolio():
    projects_data = Project.query.all()
    categories_data = Category.query.all()
    context = {
        "template_name": "site/portfolio.html",
        "template_title": "Portfolio",
        "template_body_class_name": "portfolio",
        "projects": projects_data,
        "categories": categories_data,
    }
    return context


@dp.route("/resume")
@htmx_route()
def resume():
    resume_ = Resume.query.first()
    resume_html = None

    if resume_ is not None:
        resume_html = markdown.markdown(resume_.content)

    context = {
        "template_name": "site/resume.html",
        "template_title": "Resume",
        "template_body_class_name": "resume",
        "resume_html": resume_html,
        "resume": resume_,
    }
    return context


@dp.route("/resume/download/<int:resume_id>")
def download_resume(resume_id):
    get_resume_in_db = Resume.query.get(resume_id)
    if get_resume_in_db is None:
        abort(404)
    return send_from_directory(
        config.UPLOAD_FOLDER, get_resume_in_db.file, as_attachment=True
    )


@dp.route("/services")
@htmx_route()
def services():
    services_data = Service.query.all()

    context = {
        "template_name": "site/services.html",
        "template_title": "Services",
        "template_body_class_name": "contact",
        "services": services_data,
    }
    return context


@dp.route("/service-detail/<int:service_id>")
@htmx_route()
def service_detail(service_id):
    service_data = Service.query.get(service_id)
    context = {
        "template_name": "site/service_detail.html",
        "template_title": service_data.name,
        "template_body_class_name": "services-detail",
    }
    return context


@dp.route("/starter")
def starter():
    return render_template("site/starter_page.html")
