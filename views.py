from flask import Flask, render_template, redirect, url_for

from Forms import *

app = Flask(__name__)

app.config['SECRET_KEY'] = b'\x9e\x8d\x9a\x91\ts\x0b\xa8\x17\x01\xffe\\\xc4\xf1\xb7\xec#\xcf\x96\x14\xacs\x9f'


@app.route("/welcome", methods=['GET', 'POST'])
def welcome():
    form = Information()
    if form.validate_on_submit():
        return render_template("generateTable.html", form=form)
    return render_template("firstPage.html", form=form)

# @app.route("/testReport", methods=['GET'])
# def report(form):
#     return render_template("generateTable.html", form=form)
