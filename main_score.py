
from flask import Flask

from score import get_score
from html_score_utils import *

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        score = get_score()
        return score_html_page(score)
    except Exception as ex:
        return error_html_page(ex)
