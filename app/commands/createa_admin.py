from flask.cli import with_appcontext
from werkzeug.security import generate_password_hash

from app.models import User
from app.extensions import db

import click


@click.command("create-admin")
@click.argument("username")
@click.argument("email")
@click.argument("password")
@with_appcontext
def create_admin(username, email, password):
    user = User(
        username=username,
        email=email,
        password=generate_password_hash(password),
        is_admin=True,
    )
    db.session.add(user)
    db.session.commit()
    click.echo(f"Admin user {username} created successfully.")
