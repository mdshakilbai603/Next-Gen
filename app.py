from flask import Flask, render_template, request, jsonify
from image_engine import get_image_url
from audio_engine import get_audio_url

app = Flask(__name__, template_folder=".")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.get_json()
        if not data:
            return jsonify({'error': 'Invalid request'}), 400
            
        prompt = data.get('prompt')
        mode = str(data.get('mode', '')).lower()
        ratio = data.get('ratio', '1:1')
        
        if not prompt:
            return jsonify({'error': 'Prompt missing'}), 400
            
        # যদি ইউজার অডিও/মিউজিক বা ভয়েস সিলেক্ট করে থাকে
        if 'audio' in mode or 'music' in mode or 'voice' in mode:
            audio_url = get_audio_url(prompt)
            if audio_url:
                return jsonify({'result': audio_url})
            else:
                return jsonify({'error': 'Audio generation failed'}), 500
                
        # অন্যথায় ইমেজ জেনারেশন
        else:
            image_url = get_image_url(prompt, ratio)
            if image_url:
                return jsonify({'result': image_url})
            else:
                return jsonify({'error': 'Image generation failed'}), 500
                
    except Exception as e:
        return jsonify({'error': f'Server Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
