from flask import Flask, render_template
from SolutionTwo.Form import Information

app = Flask(__name__)


@app.route("/")
def welcome():
    form = Information()
    if form.validate_on_submit():
        # tests = form.tests.data
        # phoneModel = form.phoneModel.data
        # phoneOS = form.phoneOS.data
        # device = form.device.data
        # FirmwareVersion = form.firmwareVersion.data
        return render_template("generateTable.html", form=form)
    return render_template("index.html")
