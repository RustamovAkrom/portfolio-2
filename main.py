from flask import request
import logging
import git
from app import create_app
from app.config import config


if config.DEBUG:
    logging.basicConfig(level=logging.DEBUG)


app = create_app()


@app.route("/update_server", methods=["POST"])
def webhook():
    if request.method == "POST":
        repo = git.Repo("mysite")
        origin = repo.remotes.origin
        origin.pull()
        return "Updated PythonAnywhere successfully", 200
    else:
        return "Wrong event type", 400
