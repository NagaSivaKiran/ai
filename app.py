from flask import Flask, render_template, request, jsonify  # <-- Add render_template here
import requests

app = Flask(__name__)

# Flask route to serve the HTML page
@app.route('/')
def index():
    return render_template('index.html')  # This will render the index.html file

# Flask route for handling chat queries
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = f"Response to: {user_input}"
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)
