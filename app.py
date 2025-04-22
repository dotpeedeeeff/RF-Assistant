from rf import RFfun
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "dfkl2345"

@app.route("/hello")
def hello():
    return render_template("test.html")

@app.route("/lc")
def lc():
    return render_template("index.html", len=0, output=0)


@app.route("/freq", methods=["POST", "GET"])
def freq_display():
    user_ind = float(request.form['inductance'])
    ind_suff = str(request.form['prefixhenries'])
    cap_start = float(request.form['startcapacitance'])
    cap_stop = float(request.form['stopcapacitance'])
    cap_step = float(request.form['capacitancestep'])
    cap_suff = str(request.form['prefixcapacitance'])

    message = "For Inductance of " + str(user_ind) + " " + ind_suff

    output = RFfun.freq_finder(user_ind, ind_suff, cap_start, cap_stop, cap_step, cap_suff)
    return render_template("index.html", len=len(output), output=output, message=message)