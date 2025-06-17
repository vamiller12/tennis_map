from flask import Flask, jsonify
import json

app = Flask(__name__)

# Load geolocation data from a file
with open('../data/locations.json') as f:
    locations = json.load(f)

@app.route('/api/locations', methods=['GET'])
def get_locations():
    return jsonify(locations)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=53381)