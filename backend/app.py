from flask import Flask, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}}); #Allow CORS for the React frontend

@app.route('/')
def home():
    return jsonify("Welcome to the Flask backend!")    

@app.route('/api/hello')
def hello():
    return jsonify({"message": "Hello EiSandyphyo from Flask backend!"})    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 5001)), debug=True)