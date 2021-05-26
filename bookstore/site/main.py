from flask import render_template, Blueprint, redirect
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
    form.category.choices = Category.query.all()
    if form.validate_on_submit():
        add_book(
            title=form.title.data,
            author=form.author.data,
            category=form.category.data,
        )
        
        return redirect("/")

    return render_template("registrations.html", form=form)


@bp.route("/login", methods=["GET", "POST"])
def login():
    return render_template("index.html")


@bp.route("/books")
def books():
    books = Book.query.all()

    return render_template("books.html", books=books)


@bp.route("/search")
def search():
    form = SearchForm()
    form.filter.choices = ['Title', 'Author', 'Category']
    if form.validate_on_submit():
        search_book(
            options=form.filter.data,
            word=form.string.data,
                )

    return render_template("search.html", form=form)

        