import requests
import base64

def get_audio_url(prompt):
    """
    Hugging Face-এর Meta MusicGen মডেল ব্যবহার করে গান/মিউজিক তৈরির লজিক।
    """
    try:
        if not prompt:
            return None

        # Meta-র MusicGen মডেলের জন্য ফ্রি এপিআই ইউআরএল
        API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
        
        # প্রম্পট অনুযায়ী মিউজিক রিকোয়েস্ট
        payload = {"inputs": prompt}
        response = requests.post(API_URL, json=payload, timeout=60)
        
        if response.status_code == 200:
            # অডিও ফাইল বাইনারি থেকে Base64 ডেটাতে রূপান্তর (যা সরাসরি HTML5 অডিও প্লেয়ারে চলে)
            audio_bytes = response.content
            base64_audio = base64.b64encode(audio_bytes).decode('utf-8')
            return f"data:audio/wav;base64,{base64_audio}"
        else:
            return None

    except Exception as e:
        print("Audio Generation Error:", str(e))
        return None
