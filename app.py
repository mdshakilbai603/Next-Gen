from flask import Flask, render_template, request, jsonify
from image_engine import get_image_url

app = Flask(__name__, template_folder=".")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'Invalid request'}), 400
        
    prompt = data.get('prompt')
    ratio = data.get('ratio', '1:1')
    
    if not prompt:
        return jsonify({'error': 'Prompt missing'}), 400
    
    image_url = get_image_url(prompt, ratio)
    
    if image_url:
        return jsonify({'result': image_url})
    else:
        return jsonify({'error': 'Generation failed'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
