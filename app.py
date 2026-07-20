from flask import Flask, render_template, request, jsonify
from image_engine import get_image_url

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
        ratio = data.get('ratio', '1:1')
        file_url = data.get('fileUrl')    # ফ্রন্টএন্ড থেকে আপলোড করা ইমেজ বা ফাইলের Base64 ডেটা
        file_name = data.get('fileName')  # ফাইলের নাম
        
        # প্রম্পট অথবা আপলোড করা ফাইল—যেকোনো একটি থাকলেই জেনারেশন শুরু হবে
        if not prompt and not file_url:
            return jsonify({'error': 'Prompt or File missing'}), 400
        
        # image_engine-এর নতুন লজিকে ৪টি প্যারামিটারই পাস করা হলো
        image_url = get_image_url(prompt, ratio, file_url, file_name)
        
        if image_url:
            return jsonify({'result': image_url})
        else:
            return jsonify({'error': 'Generation failed'}), 500
            
    except Exception as e:
        return jsonify({'error': f'Server Error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
