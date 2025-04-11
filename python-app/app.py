import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return f'Hello World from your local Minikube Cluster!Test'  # Proper string formatting

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

