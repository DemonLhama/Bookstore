from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired


class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])

    author = StringField("Author", validators=[DataRequired()])

    category = StringField("Category", validators=[DataRequired()])
