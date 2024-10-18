from flask import Blueprint, render_template, abort, send_from_directory
from app.models import Resume, About, Skill, Service, Project, Category
from app.config import config

import markdown


dp = Blueprint("site", __name__)

@dp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(config.UPLOAD_FOLDER, filename)


@dp.route('/')
@dp.route('/home')
def index():
    return render_template("site/index.html")


@dp.route('/about')
def about():
    about_data = About.query.first()
    skills_data = Skill.query.all()
    skills_count = len(skills_data) // 2
    left_skills = skills_data[:skills_count]
    right_skills = skills_data[skills_count:]

    context={
        "about": about_data,
        "left_skills": left_skills,
        "right_skills": right_skills
    }
    return render_template('site/about.html', **context)


@dp.route('/contact')
def contact():
    return render_template('site/contact.html')


@dp.route('/portfolio')
def portfolio():
    projects_data = Project.query.all()
    categories_data = Category.query.all()
    context = {
        "projects": projects_data,
        "categories": categories_data
    }
    return render_template('site/portfolio.html', **context)


@dp.route('/portfolio/details/<int:portfolio_id>')
def portfolio_details(portfolio_id):
    project_data = Project.query.get(portfolio_id)
    return render_template('site/portfolio_detail.html', project=project_data)


@dp.route('/resume')
def resume():
    resume_ = Resume.query.first()
    resume_html = None

    if resume_ is not None:
        resume_html = markdown.markdown(resume_.content)

    return render_template('site/resume.html', 
        resume_html=resume_html,
        resume=resume_
    )

@dp.route('/resume/download/<int:resume_id>')
def download_resume(resume_id):
    get_resume_in_db = Resume.query.get(resume_id)
    if get_resume_in_db is None:
        abort(404)
    return send_from_directory(config.UPLOAD_FOLDER, get_resume_in_db.file, as_attachment=True)


@dp.route('/services')
def services():
    services_data = Service.query.all()
    return render_template('site/services.html', services=services_data)


@dp.route('/service-detail/<int:service_id>')
def service_detail(service_id):
    service_data = Service.query.get(id=service_id)
    return render_template('site/service_detail.html', service=service_data)


@dp.route('/starter')
def starter():
    return render_template('site/starter_page.html')
