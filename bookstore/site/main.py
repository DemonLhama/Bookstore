from flask import render_template, Blueprint, redirect
from bookstore.catalog.form import BookForm
from bookstore.catalog.controller import add_book


bp = Blueprint("site", __name__)


@bp.route("/")
def index():
    return render_template("index.html")


@bp.route("/registrate", methods=["GET", "POST"])
def registrate():
    form = BookForm(csrf_enabled=False)
    if form.validate_on_submit():
        add_book(
            title=form.title.data,
            author=form.author.data,
            category=form.category_id.data,
        )
        
        return redirect("/")

    return render_template("registrations.html", form=form)
