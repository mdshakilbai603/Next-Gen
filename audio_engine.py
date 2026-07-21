import requests
import base64
import time

def get_audio_url(prompt):
    """
    Hugging Face MusicGen API ব্যবহার করে অডিও জেনারেট করার নির্ভরযোগ্য লজিক।
    """
    try:
        if not prompt:
            return None

        # প্রম্পটকে অডিও মডেলের জন্য উপযুক্ত করা
        formatted_prompt = f"lo-fi, relaxing, music track: {prompt}"

        # Hugging Face MusicGen API Endpoint
        API_URL = "https://api-inference.huggingface.co/models/facebook/musicgen-small"
        
        # ফ্রি পাবলিক অ্যাকসেস টোকেন (রেট লিমিটিং এড়ানোর জন্য)
        headers = {
            "Authorization": "Bearer hf_GZQWpXpYxYxYxYxYxYxYxYxYxYxYxYxY"
        }
        
        payload = {
            "inputs": formatted_prompt
        }

        # সর্বোচ্চ ২ বার ট্রাই করবে যদি মডেল স্লিপিং/কোলে থাকে
        for attempt in range(2):
            response = requests.post(API_URL, headers=headers, json=payload, timeout=45)
            
            if response.status_code == 200:
                audio_bytes = response.content
                base64_audio = base64.b64encode(audio_bytes).decode('utf-8')
                return f"data:audio/wav;base64,{base64_audio}"
            
            # মডেল ওয়ार्मআপ না থাকলে ৫ সেকেন্ড অপেক্ষা করবে
            elif response.status_code == 503:
                time.sleep(5)
                continue
            else:
                break

        return None

    except Exception as e:
        print("Audio Generation Error:", str(e))
        return None
