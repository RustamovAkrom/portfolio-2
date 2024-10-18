from flask import Blueprint, render_template, abort, send_from_directory
from app.models import Resume, About
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
    get_about_in_db = About.query.first()
    return render_template('site/about.html', about=get_about_in_db)


@dp.route('/contact')
def contact():
    return render_template('site/contact.html')


@dp.route('/portfolio')
def portfolio():
    return render_template('site/portfolio.html')


@dp.route('/portfolio/details/<int:portfolio_id>')
def portfolio_details(portfolio_id):
    return render_template('site/portfolio_detail.html')


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
    return render_template('site/services.html')


@dp.route('/starter')
def starter():
    return render_template('site/starter_page.html')
