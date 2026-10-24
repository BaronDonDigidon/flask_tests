from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import DataRequired
from functools import wraps

app = Flask(__name__)

def number_length(min: int, max: int, message: Optional[str] = None):
    def _number_length(form: FlaskForm, field: Field):
        if field.data is None:
            return
        value = field.data
        if value < 0:
            raise ValidationError(message or "Значение должно быть неотрицательным")
        length = len(str(value))
        if not (min_len <= length <= max_len):
            raise ValidationError(
                message or f"Длина числа должна быть от {min_len} до {max_len} цифр"
            )
    return _number_length

number = IntegerField(validators=[DataRequired(), number_length(10, 20)])


class NumberLength:
    def __init__(self, min_len, max_len, message=None):
        self.min_len = min_len
        self.max_len = max_len
        self.message = message

    def __call__(self, form, field):  # ← тоже обязательно form и field
        if field.data is None:
            return
        value = field.data
        if value < 0:
            raise ValidationError(self.message or "Значение должно быть неотрицательным")
        length = len(str(value))
        if not (self.min_len <= length <= self.max_len):
            raise ValidationError(
                self.message or f"Длина числа должна быть от {self.min_len} до {self.max_len} цифр"
                )


number = IntegerField(validators=[DataRequired(), NumberLength()])