import rf
from flask import Flask, render_template, request

app = Flask(__name__)
app.secret_key = "dfkl2345"



@app.route("/lc")
def lc():
    return render_template("indexstart.html", len=0, output=0)


@app.route("/")
def home():
    return render_template("home.html", len=0, output=0)


@app.route("/creact")
def creact():
    return render_template("creactstart.html", len=0, output=0)


@app.route("/cresults", methods=["POST", "GET"])
def cresults():
    user_capacitance = float(request.form['capacitance'])
    capacitance_suffix = str(request.form['suffixcapacitance'])
    frequency = float(request.form['frequency'])

    print("=== FORM DATA DEBUG ===")
    print(f"request.form: {dict(request.form)}")
    print("capacitance is", user_capacitance)
    print("capsuffix is ", capacitance_suffix)
    print("frequency is ", frequency)

    reactance_output = rf.capacitive_reactance_calculator(user_capacitance, capacitance_suffix, frequency)
    reactance_output = str(reactance_output)

    capacitance = "Capacitance: " + str(user_capacitance) + " " + capacitance_suffix
    frequency = "Frequency: " + str(int(frequency)) + " kHz"
    message = "Capacitive Reactance is: " + reactance_output + " Ω"



    return render_template("creact.html", len=0, output=0, message=message, frequency=frequency, capacitance=capacitance)


@app.route("/lreact")
def lreact():
    return render_template("lreactstart.html", len=0, output=0)


@app.route("/lresults", methods=["POST", "GET"])
def lresults():

    user_inductance = float(request.form['inductance'])
    inductance_suffix = str(request.form['suffixinductance'])
    frequency = float(request.form['frequency'])

    print("=== FORM DATA DEBUG ===")
    print(f"request.form: {dict(request.form)}")
    print("inductance is", user_inductance)
    print("indsuffix is ", inductance_suffix)
    print("frequency is ", frequency)

    reactance_output = rf.inductive_reactance_calculator(user_inductance, inductance_suffix, frequency)
    reactance_output = str(reactance_output)

    inductance = "Inductance: " + str(user_inductance) + " " + inductance_suffix
    frequency = "Frequency: " + str(int(frequency)) + " kHz"
    message = "Inductive Reactance is: " + reactance_output + " Ω"

    return render_template("lreact.html", len=0, output=0, message=message, frequency=frequency, inductance=inductance)


@app.route("/freq", methods=["POST", "GET"])
def freq_display():
    user_inductance = float(request.form['inductance'])
    inductance_suffix = "uH"
    start_capacitance = int(request.form['startcapacitance'])
    stop_capacitance = int(request.form['stopcapacitance'])
    capacitance_step = int(request.form['capacitancestep'])
    capacitance_suffix = "pF"

    """print("=== FORM DATA DEBUG ===")
    print(f"request.form: {dict(request.form)}")
    print("inductance is", user_inductance)
    print("startcap is ", start_capacitance)
    print("stopcap is ", stop_capacitance)"""

    message = "For Inductance of " + str(user_inductance) + " uH"
    output = rf.final_frequency_calculcator(user_inductance, inductance_suffix, start_capacitance, stop_capacitance, capacitance_step, capacitance_suffix)

    return render_template("index.html", len=len(output), output=output, message=message)


@app.route("/capband")
def capband():
    return render_template("capbandstart.html", len=0, output=0)


@app.route("/capresults", methods=["POST", "GET"])
def capresults():
    user_inductance = float(request.form['inductance'])
    desired_band = str(request.form['desiredband'])

    """print("=== FORM DATA DEBUG ===")
    print(f"request.form: {dict(request.form)}")
    print("inductance is", user_inductance)
    print("band is ", desired_band)"""

    capacitor_bottom, capacitor_top = rf.band_capacitor_calculator(user_inductance, desired_band)

    conditions = "Inductor of " + str(user_inductance) + " uH on the " + desired_band + " band."

    message = "Capacitor range is from " + capacitor_bottom + " to " + capacitor_top

    return render_template("capband.html", len=0, output=0, message=message, conditions=conditions)
