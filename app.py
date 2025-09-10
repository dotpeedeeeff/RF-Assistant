import rf
from flask import Flask, render_template, request
import logging

app = Flask(__name__)
app.secret_key = "dfkl2345"


@app.route("/hello")
def hello():
    return render_template("test.html")


@app.route("/lc")
def lc():
    return render_template("index.html", len=0, output=0)

@app.route("/home")
def home():
    return render_template("home.html", len=0, output=0)

@app.route("/creact")
def creact():
    return render_template("creact.html", len=0, output=0)

@app.route("/lreact")
def lreact():
    return render_template("lreact.html", len=0, output=0)



@app.route("/freq", methods=["POST", "GET"])
def freq_display():
    user_inductance = float(request.form['inductance'])
    inductance_suffix = "uH"
    start_capacitance = int(request.form['startcapacitance'])
    stop_capacitance = int(request.form['stopcapacitance'])
    capacitance_step = int(request.form['capacitancestep'])
    capacitance_suffix = "pF"

    print("=== FORM DATA DEBUG ===")
    
    print(f"request.form: {dict(request.form)}")
        
    print("inductance is", user_inductance)
    print("startcap is ", start_capacitance)
    print("stopcap is ", stop_capacitance)


    message = "For Inductance of " + str(user_inductance) + " pF"
    
    output = rf.final_frequency_calculcator(user_inductance, inductance_suffix, start_capacitance, stop_capacitance, capacitance_step, capacitance_suffix)
    return render_template("index.html", len=len(output), output=output, message=message) 

