from flask import Blueprint
from .models import User
from . import login_manager


main = Blueprint("main", __name__)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
