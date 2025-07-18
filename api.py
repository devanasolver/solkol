from flask import Flask, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)

# Path to JSON data
DATA_FILE = os.path.join(os.path.dirname(__file__), 'data', 'data.json')

@app.route('/leaderboard', methods=['GET'])
def get_leaderboard():
    try:
        if not os.path.exists(DATA_FILE):
            return jsonify({'error': 'Data file not found'}), 404
        with open(DATA_FILE, 'r') as f:
            data = json.load(f)
        if not data:
            return jsonify({'error': 'No data available'}), 404
        return jsonify(data)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Use Render's assigned port
    app.run(host='0.0.0.0', port=port, debug=True)
