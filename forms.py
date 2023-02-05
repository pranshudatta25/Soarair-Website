from flask_wtf import FlaskForm
from wtforms.fields import SubmitField, StringField
from wtforms.validators import InputRequired, email

# form used in basket


class CheckoutForm(FlaskForm):
    firstname = StringField("First Name", validators=[
                            InputRequired()], render_kw={"placeholder": "Enter your first name"})
    lastname = StringField("Last Name", validators=[InputRequired()], render_kw={
                           "placeholder": "Enter your last name"})
    street = StringField("Street Details", validators=[InputRequired()], render_kw={
                         "placeholder": "Enter your street name"})
    apartment = StringField("Apartment, Unit etc.", render_kw={
                            "placeholder": "Optional: Enter apartment details"})
    state = StringField("State", validators=[InputRequired()], render_kw={
                        "placeholder": "Enter your state"})
    zip = StringField("Postal / Zip", validators=[InputRequired()], render_kw={
                      "placeholder": "Enter your zip code"})
    email = StringField("Email Address", validators=[InputRequired(
    ), email()], render_kw={"placeholder": "Enter your email address"})
    phone = StringField("Phone Number", validators=[InputRequired()], render_kw={
                        "placeholder": "Enter your phone number"})
    notes = StringField("Order Notes", render_kw={
                        "placeholder": "Optional: Enter your notes here"})
    submit = SubmitField("Place Order")
