import urllib.parse
import requests
import base64

def get_audio_url(prompt):
    """
    ভয়েস এবং মিউজিক বা স্পিচ জেনারেট করার ইঞ্জিন।
    """
    try:
        if not prompt:
            return None

        clean_text = prompt.strip()
        encoded_prompt = urllib.parse.quote(clean_text)
        
        # মাইক্রোসফট এজ / অনলাইন স্পিচ সার্ভিস ব্যবহার করে সরাসরি অডিও জেনারেশন
        tts_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_prompt}&tl=en&client=tw-ob"
        
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
        }

        response = requests.get(tts_url, headers=headers, timeout=15)

        if response.status_code == 200:
            audio_base64 = base64.b64encode(response.content).decode('utf-8')
            return f"data:audio/mp3;base64,{audio_base64}"
            
        return None

    except Exception as e:
        print("Audio Engine Error:", str(e))
        return None
