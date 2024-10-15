from flask import Blueprint, render_template, flash, redirect, url_for, request
from app.models import User
from app import login_manager


dp = Blueprint("site", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@dp.route('/')
@dp.route('/home')
def index():
    return render_template("index.html")


@dp.route('/about')
def about():
    return render_template('about.html')


@dp.route('/contact')
def contact():
    return render_template('contact.html')


@dp.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@dp.route('/portfolio/details/{portfolio_id}')
def portfolio_details(portfolio_id):
    return render_template('portfolio_detail.html')


@dp.route('/resume')
def resume():
    return render_template('resume.html')


@dp.route('/services')
def services():
    return render_template('services.html')


@dp.route('/starter')
def starter():
    return render_template('starter_page.html')
