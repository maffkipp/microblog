'Top level project file.'
from app import app, db
from app.models import User, Post

@app.shell_context_processor
def make_shell_context():
    'Adds database and data models to shell instance.'
    return {'db': db, 'User': User, 'Post': Post}