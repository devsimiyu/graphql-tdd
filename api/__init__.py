from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.get('/health')
def hello():
    return 'Hello, world!'