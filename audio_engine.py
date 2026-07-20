import urllib.parse
import random

def get_audio_url(prompt):
    """
    প্রম্পট অনুযায়ী এআই মিউজিক/গান জেনারেট করার ডিরেক্ট লিংক তৈরি করে।
    """
    try:
        if not prompt:
            return None
            
        # অডিও ক্যাশ ভাঙার জন্য ইউনিক সিড
        random_seed = random.randint(1, 9999999)
        
        # প্রম্পটটি এনকোড করা
        encoded_prompt = urllib.parse.quote(prompt)
        
        # Pollinations AI-এর ফাস্ট এবং ফ্রি টেক্সট-টু-অডিও/মিউজিক API লিংক
        # এটি সরাসরি একটি অডিও ফাইল (.mp3/.wav) রিটার্ন করে যা HTML5 অডিও প্লেয়ারে বাজানো যায়
        audio_url = f"https://audio.pollinations.ai/p/{encoded_prompt}?seed={random_seed}"
        
        return audio_url
    except Exception:
        return None
