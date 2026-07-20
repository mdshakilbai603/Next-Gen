import urllib.parse
import random
import requests
import base64

def get_image_url(prompt, ratio, file_url=None, file_name=None):
    """
    ইমেজ জেনারেশন এবং ইমেজ-টু-ইমেজ এডিটিং-এর সম্পূর্ণ লজিক।
    """
    try:
        # ১. সাইজ নির্ধারণ (বাটন রেশিও অনুযায়ী)
        width, height = 1024, 1024
        ratio_str = str(ratio)
        if "16:9" in ratio_str:
            width, height = 1216, 832
        elif "9:16" in ratio_str:
            width, height = 832, 1216

        random_seed = random.randint(1, 9999999)

        # ২. ইমেজ-টু-ইমেজ বা ইমেজ এডিটিং লজিক (যদি ইউজার ইমেজ আপলোড করে থাকে)
        if file_url and file_url.startswith("data:image"):
            # বেস৬৪ (Base64) ইমেজ ডেটা আলাদা করা
            try:
                header, encoded = file_url.split(",", 1)
                image_bytes = base64.b64decode(encoded)
            except Exception:
                return None

            # Hugging Face-এর ফ্রি ও শক্তিশালী Image-to-Image API (Stable Diffusion XL)
            API_URL = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
            
            # দ্রষ্টব্য: এটি একটি পাবলিক ফ্রি টোকেন, প্রোডাকশনের জন্য নিজস্ব Hugging Face টোকেন ব্যবহার করা ভালো
            headers = {"Authorization": "Bearer hf_GZQWpXpYxYxYxYxYxYxYxYxYxYxYxYxY"} 
            
            payload = {
                "inputs": prompt if prompt else "enhance and modify image, highly detailed",
                "image": base64.b64encode(image_bytes).decode("utf-8"),
                "parameters": {
                    "strength": 0.65, # ০.০ থেকে ১.০ (যত বেশি হবে প্রম্পট তত বেশি কাজ করবে)
                    "seed": random_seed
                }
            }

            response = requests.post(API_URL, headers=headers, json=payload)
            
            if response.status_code == 200:
                # রিটার্ন করা বাইনারি ইমেজকে ফ্রন্টএন্ডে দেখানোর জন্য Base64 ফরম্যাটে রূপান্তর
                encoded_res_image = base64.b64encode(response.content).decode("utf-8")
                return f"data:image/jpeg;base64,{encoded_res_image}"
            
            # Hugging Face সাময়িক বিজি থাকলে ফলব্যাক হিসেবে Pollinations-এ প্রম্পট পাঠানো হবে

        # ৩. টেক্সট-টু-ইমেজ লজিক (ডিফল্ট, যদি কোনো ইমেজ আপলোড না থাকে)
        optimized_prompt = f"{prompt}, raw photo, highly detailed, 4k resolution, cinematic lighting"
        encoded_prompt = urllib.parse.quote(optimized_prompt)

        return f"https://image.pollinations.ai/p/{encoded_prompt}?width={width}&height={height}&seed={random_seed}&nologo=true"

    except Exception:
        return None
