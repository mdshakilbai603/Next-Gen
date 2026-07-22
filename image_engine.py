import urllib.parse
import random
import requests

def get_image_url(prompt, ratio, file_url=None, file_name=None):
    """
    আপলোড করা ইমেজ থেকে পাবলিক লিংক জেনারেট করে এডিটিং বট বা মডেলে পাঠানোর লজিক।
    """
    try:
        # ১. রেশিও অনুযায়ী সাইজ নির্ধারণ
        width, height = 1024, 1024
        ratio_str = str(ratio)
        
        if "16:9" in ratio_str:
            width, height = 1216, 832
        elif "9:16" in ratio_str:
            width, height = 832, 1216

        random_seed = random.randint(1, 9999999)
        clean_prompt = prompt.strip() if prompt else "enhance image"

        # ২. যদি ইউজার ছবি আপলোড করে
        if file_url:
            public_image_link = None

            # যদি ফ্রন্টএন্ড থেকে Base64 বা ডেটা ইউআরএল আসে, সেটিকে পাইথন পাবলিক লিংকে রূপান্তর করবে
            if file_url.startswith("data:image"):
                try:
                    # ফ্রি পাবলিক ইমেজ হোস্টিং (Catbox API) ব্যবহার করে পাইথন নিজেই পাবলিক লিংক তৈরি করছে
                    header, encoded = file_url.split(",", 1)
                    image_bytes = base64.b64decode(encoded) if 'base64' in globals() else __import__('base64').b64decode(encoded)
                    
                    files = {'file': (file_name if file_name else 'image.jpg', image_bytes)}
                    data = {'reqtype': 'fileupload'}
                    
                    response = requests.post("https://catbox.moe/user/api.php", data=data, files=files, timeout=15)
                    if response.status_code == 200 and response.text.startswith("http"):
                        public_image_link = response.text.strip()
                except Exception:
                    pass

            # যদি পাবলিক লিংক তৈরি হয়ে যায়, সেটি এডিটিং বট/মডেলে পাঠানো হবে
            if public_image_link:
                # এখানে জেনারেট হওয়া পাবলিক লিংক দিয়ে এডিটিং বা প্রসেসিং করা হবে
                edit_query = f"transform image {public_image_link} with style: {clean_prompt}"
                encoded_query = urllib.parse.quote(edit_query)
                return f"https://image.pollinations.ai/p/{encoded_query}?width={width}&height={height}&seed={random_seed}&nologo=true"
            
            else:
                # ফলব্যাক লিংক যদি হোস্টিং কাজ না করে
                fallback_query = f"edit uploaded image: {clean_prompt}"
                encoded_query = urllib.parse.quote(fallback_query)
                return f"https://image.pollinations.ai/p/{encoded_query}?width={width}&height={height}&seed={random_seed}&nologo=true"

        # ৩. সাধারণ টেক্সট-টু-ইমেজ জেনারেশন
        encoded_prompt = urllib.parse.quote(clean_prompt)
        return f"https://image.pollinations.ai/p/{encoded_prompt}?width={width}&height={height}&seed={random_seed}&nologo=true"

    except Exception as e:
        print("Engine Error:", str(e))
        return None
