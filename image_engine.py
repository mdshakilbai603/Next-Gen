import urllib.parse
import random

def get_image_url(prompt, ratio):
    """
    ইমেজ জেনারেশনের সম্পূর্ণ লজিক।
    """
    try:
        width, height = 1024, 1024
        if ratio == "16:9":
            width, height = 1216, 832
        elif ratio == "9:16":
            width, height = 832, 1216

        # প্রম্পট ক্যাশ ভাঙার জন্য ইউনিক সিড
        random_seed = random.randint(1, 9999999)
        optimized_prompt = f"{prompt}, raw photo, highly detailed, cinematic lighting --seed {random_seed}"
        encoded_prompt = urllib.parse.quote(optimized_prompt)

        return f"https://image.nofilter.ai/prompt/{encoded_prompt}?width={width}&height={height}&model=flux-speed&nologo=true"
    except Exception:
        return None
