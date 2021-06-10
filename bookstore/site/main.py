from flask import render_template, Blueprint, redirect, url_for, flash
from bookstore.db.models import *
from bookstore.catalog.form import BookForm
from bookstore.catalog.controller import add_book


bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/registrate", methods=["GET", "POST"])
def registrate():
    form = BookForm()
    form.category.choices = CategoryTable.query.all()
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
    books = BookTable.query.all()

    return render_template("books.html", books=books)





