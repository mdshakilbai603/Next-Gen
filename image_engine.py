import urllib.parse
import random

def get_image_url(prompt, ratio):
    """
    ইমেজ জেনারেশনের সম্পূর্ণ লজিক (১০০% কার্যকরী ডিরেক্ট ইমেজ লিংক)।
    """
    try:
        # ডিফল্ট সাইজ (১:১ স্কয়ার)
        width, height = 1024, 1024
        
        ratio_str = str(ratio)
        
        # ফ্রন্টএন্ডের বাটনের টেক্সট অনুযায়ী সাইজ নির্ধারণ
        if "16:9" in ratio_str:
            width, height = 1216, 832
        elif "9:16" in ratio_str:
            width, height = 832, 1216
        else:
            width, height = 1024, 1024

        # প্রতিবার নতুন ইমেজ পাওয়ার জন্য র্যান্ডম সিড
        random_seed = random.randint(1, 9999999)
        
        # প্রম্পটটিকে সুন্দর ও অপ্টিমাইজ করা
        optimized_prompt = f"{prompt}, raw photo, highly detailed, 4k resolution, cinematic lighting"
        encoded_prompt = urllib.parse.quote(optimized_prompt)

        # Pollinations AI-এর ডিরেক্ট ইমেজ জেনারেটর ইউআরএল (যা সরাসরি <img> ট্যাগ সাপোর্ট করে)
        return f"https://image.pollinations.ai/p/{encoded_prompt}?width={width}&height={height}&seed={random_seed}&nologo=true"
    except Exception:
        return None
