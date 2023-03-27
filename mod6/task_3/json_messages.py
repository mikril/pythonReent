import logging
import json
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField
from wtforms.validators import InputRequired
from datetime import datetime


class JsonAdapter(logging.LoggerAdapter):
    def process(self, msg, kwargs):
        message = json.dumps(msg)
        return message, kwargs

logger = JsonAdapter(logging.getLogger(__name__))
log = logging.getLogger('werkzeug')
log.disabled = True
app = Flask(__name__)


class DivideFrom(FlaskForm):
    a = IntegerField(validators=[InputRequired()])
    b = IntegerField(validators=[InputRequired()])

@app.route("/divide/", methods=["POST"])
def divide():
    form = DivideFrom()
    if form.validate_on_submit():
        a, b = form.a.data, form.b.data

        logger.debug(f"From is valid. a={a}, b={b}")

        return f"a / b = {a / b:2f}"
    logger.error(f"Form is not valid, error={form.errors}")
    return f"Bad request", 400

@app.errorhandler(ZeroDivisionError)
def handle_exception(e: ZeroDivisionError):
    logger.exception('We are unable "to divide by zero!', exc_info=e)
    return "We are unable to divide by zero!", 400

if __name__=="__main__":
    logging.basicConfig(filename='skillbox_json_messages.log',format='{"time":"%(asctime)s", "level": "%(levelname)s", "message": %(message)s}', level=logging.INFO,datefmt='%H:%M:%S',)
    app.config["WTF_CSRF_ENABLED"] = False
    app.run(debug=True)
    logger.info('Сообщение')