from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow frontend to access backend

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get('message', '').lower()

    if "hello" in message:
        response = "Hi there!"
    elif "how are you" in message:
        response = "I'm just a bot, but I'm doing great!"
    else:
        response = "I don't understand that yet."

    return jsonify({'response': response})

if __name__ == '__main__':
    app.run()
    