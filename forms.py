"""Form class declaration."""
from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    DateField,
    PasswordField,
    SelectField,
    StringField,
    SubmitField,
    TextAreaField,
)
from datetime import date
from wtforms.validators import DateField, URL, DataRequired, Email, EqualTo, Length

class StockForm(FlaskForm):
    """Generate Your Graph."""

    #THIS IS WHERE YOU WILL IMPLEMENT YOUR CODE TO POPULATE THE SYMBOL FIELD WITH STOCK OPTIONS
    symbol = SelectField("Choose Stock Symbol", [DataRequired()],
        choices=[
            ("IBM", "IBM"),
            ("GOOGL", "GOOGL"),
        ],
    )

    chart_type = SelectField("Select Chart Type",[DataRequired()],
        choices=[
            ("1", "1. Bar"),
            ("2", "2. Line"),
        ],
    )

    time_series = SelectField("Select Time Series",[DataRequired()],
        choices=[
            ("1", "1. Daily"),
            ("2", "2. Monthly"),
            ("3", "3. Yearly"),
            ("4", "4. Intraday"),
        ],
    )

    start_date = DateField("Enter Start Date")
    end_date = DateField("Enter End Date")
    submit = SubmitField("Submit")
