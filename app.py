from flask import Flask, request, jsonify
from anki_helpers import add_card

app = Flask(__name__)

@app.route('/add_card', methods=['POST'])
def add_card_endpoint():
    data = request.json
    deck_name = data.get('deck_name')
    front = data.get('front')
    back = data.get('back')
    
    if not deck_name or not front or not back:
        return jsonify({'error': 'Missing required fields'}), 400
    
    try:
        card_id = add_card(deck_name, front, back)
        return jsonify({'status': 'success', 'card_id': card_id}), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
