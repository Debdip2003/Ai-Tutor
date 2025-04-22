from flask import Flask, request, jsonify,render_template
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return render_template('index.html')
@app.route('/ask', methods=['POST'])
def ask_tutor():
    data = request.get_json()
    user_query = data.get('query')

    prompt = f"You are an AI tutor helping artisans build eco-friendly products, sustainable packaging, and pricing strategies. Answer this query: {user_query}"

   
    payload = {
        "model": "mistral", 
        "prompt": prompt,
        "stream": False
    }

    response = requests.post("http://localhost:11434/api/generate", json=payload)

    if response.status_code == 200:
        reply = response.json()['response']
        return jsonify({'reply': reply})
    else:
        return jsonify({'error': 'Failed to get response from model'}), 500

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001,debug=True)