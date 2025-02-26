# Description: Main file for the project
import os

from flask import Flask, request, jsonify
from flask_cors import CORS

from src import db

app = Flask(__name__)
CORS(app)

@app.route('/api/v1/health', methods=['GET'])
def health():
    return jsonify({'status': 'ok'})

@app.route('/api/v1/insert', methods=['POST'])
def insert():
    data = request.json
    db.insert(data)
    return jsonify({'status': 'ok'})

@app.route('/api/v1/get', methods=['GET'])
def get():
    data = db.get()
    return jsonify(data)

        