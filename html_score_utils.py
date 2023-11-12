
def score_html_page(score):
    return f"""<html>
    <head>
        <title>Scores Game></title>
    </head>
    <body>
        <h1>The score is:</h1>
        <div id="score">{score}</div>
    </body>
</html>"""


def error_html_page(error):
    return f"""<html>
    <head>
        <title>Scores Game></title>
    </head>
    <body>
        <h1>ERROR:</h1>
        <div id="score" style="color:red">{error}</div>
    </body>
</html>"""

