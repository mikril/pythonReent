import os
import shlex
import subprocess

from flask import Flask, request


app = Flask(__name__)


def startHost(port):
    command = f'lsof -i :{port}'
    command = shlex.split(command)
    process = subprocess.run(command, capture_output=True).stdout.decode().split("\n")[1:-1]
    pids=[]

    for i in process:
        pids.append(int(i.split()[1]))

    if not(os.getpid() in pids):
        for i in pids:
            os.kill(i,15)
    app.run(debug=True,port=port)


if __name__ == "__main__":
    startHost(5000)