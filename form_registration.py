from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, Email, NumberRange, DataRequired, Optional

app = Flask(__name__)

class RegistrationForm(FlaskForm):
    email = StringField(validators=[
        DataRequired(message="Email обязателен"),
          Email()
          ])
    phone = IntegerField(validators=[
        DataRequired(message="Номер телефона обязателен"), 
        NumberRange(min=1000000000, max=9000000000)
        ])
    name = StringField(validators=[DataRequired(message="Имя обязательно")])
    address = StringField(validators=[DataRequired(message="Адресс обязателен")])
    index = IntegerField(validators=[
        DataRequired(message="Индекс обязателен"), 
        NumberRange(min=0,message="Индекс должен быть не отрицательным числом")
        ])
    comment = StringField(validators=[Optional()])

@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone = form.email.data, form.phone.data

        return f"Successfully registered user {email} with phone +7{phone}"

    return f"Invalid input, {form.errors}", 400

if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)