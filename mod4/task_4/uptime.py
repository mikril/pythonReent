from flask import Flask, request
app = Flask(__name__)
from datetime import datetime
from datetime import timedelta

@app.route("/uptime", methods=["GET"])
def uptime():
    with open('/proc/uptime', 'r') as f:
        UPTIME = str(timedelta(seconds=float(f.readline().split(maxsplit=1)[0]))).split(".")[0]
        return f"Current uptime is {UPTIME}"

if __name__ == "__main__":
    app.run(debug=True)