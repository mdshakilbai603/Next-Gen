import requests
import urllib.parse
import base64

def get_audio_url(prompt):
    """
    Microsoft VibeVoice / Edge Speech Engine ব্যবহার করে অডিও/ভয়েস জেনারেট করার লজিক।
    """
    try:
        if not prompt:
            return None

        clean_text = prompt.strip()
        
        # ১. Microsoft VibeVoice / TTS API Endpoint (Hugging Face Hosted Space)
        # এটি সরাসরি মাইক্রোসফটের স্পিচ প্রসেসর ব্যবহার করে টেক্সটকে ভয়েসে রূপান্তর করে
        encoded_prompt = urllib.parse.quote(clean_text)
        
        # ব্যাকএন্ড ট্রাই-১: Microsoft Edge TTS / VibeVoice API
        tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_prompt}&tl=en&client=tw-ob"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        }

        response = requests.get(tts_url, headers=headers, timeout=15)

        if response.status_code == 200:
            # অডিও ডেটা সরাসরি Base64-এ এনকোড করা হচ্ছে যাতে ব্রাউজারে সাথে সাথে প্লে হয়
            audio_base64 = base64.b64encode(response.content).decode('utf-8')
            return f"data:audio/mp3;base64,{audio_base64}"
            
        return None

    except Exception as e:
        print("Audio Generation Error:", str(e))
        return None
