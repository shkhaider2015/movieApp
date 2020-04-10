from flask import Blueprint, render_template, flash, redirect, url_for, request
from movieApp.admin.forms import LoginForm, DataSubmitForm
from movieApp.models import Movie

admin = Blueprint('admin', __name__)


@admin.route('/admin')
def my_admin():
    return render_template("admin.html", title="Admin Page")


@admin.route('/admin/add_movie', methods=['GET', 'POST'])
def add_data():
    movie = Movie()
    if request.method == 'POST':
        movie.movie_title = request.form.get('movie_title')
        movie.movie_industry = request.form.get('industry')
        movie.release_date = request.form.get('released_date')
        movie.movie_genr = request.form.getlist('GenrList')
        movie.movie_image = request.form.get('movie_image')
        movie.cast = request.form.get('cast')
        print(f"Name : {movie.movie_title} Industry : {movie.movie_industry} Date : {movie.release_date} Genr : {movie.movie_genr} image : {movie.movie_image} cast : {movie.cast} ")
    return render_template("my_custom_add_movies.html", title="Admin Page")


@admin.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    email = "shkhaider2015@gmail.com"
    password = "1234"
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == email and form.password.data == password:
            redirect(url_for('admin.add_data'))
            flash("Login successfully !", 'success')
        else:
            flash("Check email and password", 'danger')
    return render_template("admin_login.html", title="Admin Page", form=form)


@admin.route('/admin/custom_login_form', methods=['GET', 'POST'])
def custom_form():

    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        if email == 'shkhaider2015@gmail.com' and password == '1234':
            flash("Successfully Register !!", 'success')
        else:
            flash("Check you email or password", 'danger')
    return render_template('my_custom_login_form.html', title="My Own Form")
