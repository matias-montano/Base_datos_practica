import os
import signal
from flask import Flask, render_template, request, redirect
############################################################################################################
from calculadora_blueprint import calculator_blueprint

# importo el blueprint de inicio

# se ejecuta el servidor con el comando: python3 principal.py
# mirar en el navegador http://127.0.0.1:5000

app = Flask(__name__)
# ------------------------------- blueprints --------------------------------
app.register_blueprint(calculator_blueprint)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        task = request.form.get("task")
        return redirect("/")
    return render_template("index.html")

@app.route("/shutdown", methods=["POST"])
def shutdown():
    print("Server is shutting down...")
    os.kill(os.getpid(), signal.SIGINT)
    return "Server is shutting down..."

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("Server has been shut down.")