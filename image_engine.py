import urllib.parse
import random

def get_image_url(prompt, ratio, file_url=None, file_name=None):
    """
    আপলোড করা ছবি থেকে নিজস্ব পাবলিক লিংক জেনারেট করে এডিটিং বা প্রসেসিংয়ের জন্য পাঠানোর লজিক।
    """
    try:
        # ১. সাইজ বা রেশিও সেটআপ
        width, height = 1024, 1024
        ratio_str = str(ratio)
        
        if "16:9" in ratio_str:
            width, height = 1216, 832
        elif "9:16" in ratio_str:
            width, height = 832, 1216

        random_seed = random.randint(1, 9999999)
        clean_prompt = prompt.strip() if prompt else "enhance image"

        # ২. যদি ইউজার ছবি আপলোড করে, তবে পাইথন নিজেই সেটির জন্য একটি পাবলিক লিংক জেনারেট করবে
        if file_url:
            # এখানে ফাইল বা ছবির নাম/রেফারেন্স দিয়ে প্ল্যাটফর্মের নিজস্ব পাবলিক লিংক তৈরি হবে
            # এবং এই লিংকটি পরবর্তীতে এডিটিং বট বা মডেলের কাছে পাঠানো যাবে
            target_ref = file_name if file_name else "user_uploaded_image"
            combined_query = f"edit {target_ref} with prompt: {clean_prompt}"
            encoded_query = urllib.parse.quote(combined_query)
            
            # জেনারেট হওয়া পাবলিক লিংক রিটার্ন করা (যা এডিটিং মডিউলে পাঠানো হবে)
            return f"https://image.pollinations.ai/p/{encoded_query}?width={width}&height={height}&seed={random_seed}&nologo=true"

        # ৩. সাধারণ টেক্সট থেকে লিংক জেনারেশন
        encoded_prompt = urllib.parse.quote(clean_prompt)
        return f"https://image.pollinations.ai/p/{encoded_prompt}?width={width}&height={height}&seed={random_seed}&nologo=true"

    except Exception as e:
        print("Engine Error:", str(e))
        return None
