from flask import Blueprint, render_template, flash, redirect, url_for
from movieApp.admin.forms import LoginForm

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def my_admin():
    return render_template("admin.html", title="Admin Page")


@admin.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    email = "shkhaider2015@gmail.com"
    password = "1234"
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == email and form.password.data == password:
            redirect(url_for('admin.add_movies'))
            flash("Login successfully !", 'success')
        else:
            flash("Check email and password", 'danger')
    return render_template("admin_login.html", title="Admin Page", form=form)


@admin.route('/admin/add_movie')
def add_movies():
    return render_template("add_movies.html", title="Admin Page")