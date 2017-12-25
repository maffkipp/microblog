'Contains all error handlers.'
from flask import render_template
from app import app, db

@app.errorhandler(404)
def not_found_error(error):
    '404 error handler.'
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    '500 error handler, rolls back current database session.'
    db.session.rollback()
    return render_template('500.html'), 500
