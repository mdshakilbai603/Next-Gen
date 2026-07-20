import urllib.parse
import random

def get_image_url(prompt, ratio):
    """
    ইমেজ জেনারেশনের সম্পূর্ণ লজিক।
    """
    try:
        width, height = 1024, 1024
        
        # ফ্রন্টএন্ড থেকে আসা রেশিওর টেক্সট হ্যান্ডেল করার জন্য (যেমন: "16:9 Landscape" থেকে "16:9" নেওয়া)
        ratio_str = str(ratio)
        
        if "16:9" in ratio_str:
            width, height = 1216, 832
        elif "9:16" in ratio_str:
            width, height = 832, 1216
        else:
            width, height = 1024, 1024 # ১:১ বা স্কয়ারের জন্য default

        # প্রম্পট ক্যাশ ভাঙার জন্য ইউনিক সিড
        random_seed = random.randint(1, 9999999)
        optimized_prompt = f"{prompt}, raw photo, highly detailed, cinematic lighting --seed {random_seed}"
        encoded_prompt = urllib.parse.quote(optimized_prompt)

        return f"https://image.nofilter.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux-speed&nologo=true"
    except Exception:
        return None
