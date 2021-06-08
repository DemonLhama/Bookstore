from flask_wtf import FlaskForm
from wtforms import StringField, SelectField
from wtforms.validators import DataRequired




class BookForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired()])

    author = StringField("Author", validators=[DataRequired()])

    category = SelectField("Category", choices=[])
