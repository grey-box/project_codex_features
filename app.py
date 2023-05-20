from flask import Flask, request, jsonify
from flask_cors import CORS
from transliterate import translit

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

@app.route('/api/phonetic-transcription/<text>', methods=['GET'])
def get_phonetic_transcription(text):
    try:
        transcription = translit(text, 'uk', reversed=True)
        return jsonify({'phonetic_transcription': transcription})
    except Exception as e:
        return jsonify({'phonetic_transcription': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
