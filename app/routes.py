from flask import Blueprint, render_template, flash, redirect, url_for, request
from .models import User
from . import login_manager


main = Blueprint("main", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@main.route('/')
@main.route('/home')
def index():
    return render_template("index.html")


@main.route('/about')
def about():
    return render_template('about.html')


@main.route('/contact')
def contact():
    return render_template('contact.html')


@main.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')


@main.route('/portfolio/details/{portfolio_id}')
def portfolio_details(portfolio_id):
    return render_template('portfolio_detail.html')


@main.route('/resume')
def resume():
    return render_template('resume.html')


@main.route('/services')
def services():
    return render_template('services.html')


@main.route('/starter')
def starter():
    return render_template('starter_page.html')
