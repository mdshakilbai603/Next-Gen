import urllib.parse
import random

def get_audio_url(prompt):
    """
    ফ্রি এবং ইনস্ট্যান্ট অডিও জেনারেটর (কোনো API Key বা টোকেন লাগবে না)
    """
    try:
        if not prompt:
            return None

        # ১. প্রম্পট অপটিমাইজেশন ও এনকোডিং
        random_seed = random.randint(1000, 99999)
        clean_prompt = prompt.strip()
        encoded_prompt = urllib.parse.quote(clean_prompt)

        # ২. অডিও সার্ভার ডাইরেক্ট স্ট্রিম লিংক
        # এটি সরাসরি একটি আসল MP3 অডিও ফাইল স্ট্রিম করে যা অডিও প্লেয়ারে বাজবে
        audio_url = f"https://text.pollinations.ai/{encoded_prompt}?model=audio&seed={random_seed}"

        return audio_url

    except Exception as e:
        print("Audio Generation Error:", str(e))
        return None
