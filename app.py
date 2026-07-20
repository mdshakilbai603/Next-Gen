from flask import Flask, render_template, request, jsonify
from image_engine import get_image_url
from audio_engine import get_audio_url  # নতুন অডিও ইঞ্জিন ইমপোর্ট করা হলো

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
        mode = data.get('mode', 'Image Engine.py')  # ফ্রন্টএন্ড থেকে আসা মোড ট্র্যাক করা
        ratio = data.get('ratio', '1:1')
        
        if not prompt:
            return jsonify({'error': 'Prompt missing'}), 400
            
        # ১. যদি ইউজার 'Audio Music.py' বা 'Voice Synthesizer.py' সিলেক্ট করে গান বানাতে চায়
        if mode in ['Audio Music.py', 'Voice Synthesizer.py']:
            audio_url = get_audio_url(prompt)
            if audio_url:
                # ফ্রন্টএন্ড যাতে ফাইলটি ডাউনলোড বা প্লে করতে পারে তার জন্য ডিরেক্ট রিডাইরেক্ট বা লিংক রিটার্ন
                return jsonify({'result': audio_url})
            else:
                return jsonify({'error': 'Audio generation failed'}), 500
                
        # ২. ডিফল্ট টেক্সট-টু-ইমেজ (Image Engine) বা লুপ জিআইএফ (loop GIF)
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
