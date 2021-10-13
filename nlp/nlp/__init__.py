"""NLP package initializer."""
import os
print(os.path.dirname(os.path.abspath(__file__)))
import flask
from nlp.config import NLP_SERVER_PORT, BACKEND_SERVER_PORT

# app is a single object used by all the code modules in this package
app = flask.Flask("nlp")  # pylint: disable=invalid-name
app.config.from_object('nlp.config')

import nlp.api