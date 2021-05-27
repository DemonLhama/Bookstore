from flask import render_template, Blueprint, redirect, request, url_for, flash
from flask_login import login_user, logout_user, login_required
from bookstore.db.models import *
from bookstore.catalog.form import BookForm
from bookstore.auth.loginform import LoginForm
from bookstore.catalog.controller import add_book


bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/registrate", methods=["GET", "POST"])
def registrate():
    form = BookForm()
    form.category.choices = Category.query.all()
    if form.validate_on_submit():
        add_book(
            title=form.title.data,
            author=form.author.data,
            category=form.category.data,
        )
        return redirect (url_for('site.index'))
    flash('Book registered with sucess!')
    return render_template("registrations.html", form=form)


@bp.route("/books")
def books():
    books = Book.query.all()

    return render_template("books.html", books=books)


@bp.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, form.remember_me.data)
            next = request.args.get('next')
            if next is None or not next.startswith("/"):
                next = url_for('site.index')
            return redirect (next)
        flash('Invalid username or password.')
    return render_template('log_in.html', form=form)


@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect("/")