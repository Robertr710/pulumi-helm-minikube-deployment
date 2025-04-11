import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    # Get the POD_NAME environment variable, or use a default value if not set
    pod_name = os.getenv("POD_NAME", "Unknown")
    return f'Hello from AWS EKS pod {pod_name}, World!'  # Proper string formatting

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)

