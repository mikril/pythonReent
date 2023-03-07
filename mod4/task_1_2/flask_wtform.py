from typing import Optional

from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, Field
from wtforms.validators import InputRequired, Email, NumberRange, ValidationError

app = Flask(__name__)

class NumberLength:
    def __init__(self,min,max,message):
        self.max=max
        self.min = min
        self.message = message
    def __call__(self, form: FlaskForm, field: Field):
        if len(str(field.data))<self.min or len(str(field.data))>self.max:
            raise ValidationError(message=self.message)

def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if len(str(field.data))<min or len(str(field.data))>max:
            raise ValidationError(message=message)
    return _number_length

class RegistrationForm(FlaskForm):
    email = StringField(validators=[InputRequired(), Email()])
    phone = IntegerField(validators=[InputRequired(), NumberLength(10, 10, "wrong length")])
    name = StringField(validators=[InputRequired()])
    address = StringField(validators=[InputRequired()])
    index = IntegerField(validators=[InputRequired()])
    comment = StringField()


@app.route("/registration", methods=["POST"])
def registration():
    form = RegistrationForm()

    if form.validate_on_submit():
        email, phone,name,address ,index,comment = form.email.data, form.phone.data,form.name.data,form.address.data,form.index.data,form.comment.data

        return f"Successfully registered user {email} with phone +7{phone}"
    return f"Invalid input, {form.errors}", 400



if __name__ == "__main__":
    app.config["WTF_CSRF_ENABLED"]=False
    app.run(debug=True)