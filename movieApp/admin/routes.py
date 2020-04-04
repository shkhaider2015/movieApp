from flask import Blueprint, render_template
from movieApp.admin.forms import LoginForm

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def admin():
    return render_template("admin.html", title="Admin Page")


@admin.route('/admin/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    return render_template("admin_login.html", title="Admin Page", form=form)
