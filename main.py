from flask import Flask, request
import logging
import git
from app import create_app


logging.basicConfig(level=logging.DEBUG)


app = create_app().run(
    host="127.0.0.1",
    port=8000,
    debug=True
)

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('mysite')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return "Wrong event type", 400

