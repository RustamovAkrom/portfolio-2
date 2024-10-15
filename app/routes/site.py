from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.models import User
from app import login_manager


dp = Blueprint("site", __name__)


@dp.route('/')
@dp.route('/home')
def index():
    return render_template("site/index.html")


@dp.route('/about')
def about():
    return render_template('site/about.html')


@dp.route('/contact')
def contact():
    return render_template('site/contact.html')


@dp.route('/portfolio')
def portfolio():
    return render_template('site/portfolio.html')


@dp.route('/portfolio/details/{portfolio_id}')
def portfolio_details(portfolio_id):
    return render_template('site/portfolio_detail.html')


@dp.route('/resume')
def resume():
    return render_template('site/resume.html')


@dp.route('/services')
def services():
    return render_template('site/services.html')


@dp.route('/starter')
def starter():
    return render_template('site/starter_page.html')
