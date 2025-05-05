from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

LOG_FILE = 'mcp_log.json'

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/api/logs')
def get_logs():
    if not os.path.exists(LOG_FILE):
        return jsonify([])
    with open(LOG_FILE, 'r') as f:
        logs = json.load(f)
    return jsonify(logs)

if __name__ == '__main__':
    app.run(debug=True)