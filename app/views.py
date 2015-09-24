from flask import render_template
from logging import Formatter, FileHandler
import logging
from app import app
from app.models import Task
from app.forms import PostForm, AddForm

@app.route('/')
def home():
    form = PostForm()
    tasks = Task.query.all()
    return render_template('main.html', form=form, tasks=tasks)


@app.route('/add', methods=['GET', 'POST'])
def add():
    form = AddForm()
    print form.text._value()
    print form.title._value()

    return render_template('new.post.html',
                           title='Add new',
                           form=form)

@app.route('/about')
def about():
    return render_template('about.html')

@app.errorhandler(500)
def internal_error(error):
    return render_template('errors/500.html'), 500

@app.errorhandler(404)
def not_found_error(error):
    return render_template('errors/404.html'), 404


def log():
    file_handler = FileHandler('app.log')
    file_handler.setFormatter(
        Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]')
    )
    app.logger.setLevel(logging.INFO)
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)

log()