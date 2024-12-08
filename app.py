from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

messages = [
    {"id": 1, "sender": "Character A", "message": "Hello, how are you?", "timestamp": "10:00 AM"},
    {"id": 2, "sender": "Character B", "message": "I'm good, thank you! What about you?", "timestamp": "10:01 AM"},
    {"id": 3, "sender": "Character A", "message": "Doing great, excited to start this project.", "timestamp": "10:02 AM"}
]

@app.route('/api/messages', methods=['GET'])
def get_messages():
    return jsonify(messages)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
