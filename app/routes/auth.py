from flask import Blueprint, render_template, flash, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from app.forms import LoginForm, RegistrationForm
from app.models import User
from app import login_manager, db


dp = Blueprint("auth", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@dp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("site.index"))

    form = LoginForm()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = User.query.filter_by(username=form.username.data).first()
            print(user.username, user.password)
            if user and check_password_hash(user.password, form.password.data):
                login_user(user, remember=True)
                next_page = request.args.get("next")
                flash(f"Successfully sign in {user}", "success")
                return redirect(next_page) if next_page else redirect(url_for("site.index"))
        
        flash(f"Invalid Login. Pleace check username or password", "danger")
        
    return render_template("auth/login.html", form=form)


@dp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("site.index"))

    form = RegistrationForm()

    if form.validate_on_submit():
        user = User(
            first_name=form.first_name.data,
            last_name=form.last_name.data,
            username=form.username.data,
            email=form.email.data,
            password=generate_password_hash(form.password.data),
        )
        db.session.add(user)
        db.session.commit()

        flash("User successfully registered", "success")
        return redirect(url_for("auth.login"))

    return render_template("auth/register.html", form=form)


@dp.route("/logout", methods=["GET", "POST"])
@login_required
def logout():
    logout_user()
    return redirect(url_for("site.index"))
