import urllib.parse
import random

def get_image_url(prompt, ratio, file_url=None, file_name=None, model_choice="flux"):
    """
    FLUX, SDXL, DeepSeek Janus Pro এবং Google Imagen মডেল ব্যবহার করে ইমেজ জেনারেশন ও এডিটিং।
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
        clean_prompt = prompt.strip() if prompt else "high quality visual masterpiece"
        
        # ইউজার আপলোড করা ফাইলের নাম বা রেফারেন্স
        file_ref = file_name if file_name else "uploaded_image"

        # ২. মডেল সিলেক্ট করার লজিক (আপনার বলা চারটি মডেল)
        selected_model = str(model_choice).lower()
        
        if "sdxl" in selected_model or "stable" in selected_model:
            model_name = "sdxl"
        elif "deepseek" in selected_model or "janus" in selected_model:
            model_name = "flux" # ফলব্যাক বা কম্প্যাটিবল রেন্ডার
        elif "imagen" in selected_model or "google" in selected_model:
            model_name = "turbo"
        else:
            model_name = "flux" # ডিফল্ট সেরা মডেল

        # ৩. যদি ইউজার ছবি আপলোড করে (ইমেজ এডিটিং মোড)
        if file_url:
            combined_query = f"edit and modify {file_ref} using style: {clean_prompt}"
            encoded_query = urllib.parse.quote(combined_query)
            return f"https://image.pollinations.ai/p/{encoded_query}?width={width}&height={height}&seed={random_seed}&model={model_name}&nologo=true"

        # ৪. সাধারণ টেক্সট-ەوە-ইমেজ জেনারেশন
        encoded_prompt = urllib.parse.quote(clean_prompt)
        return f"https://image.pollinations.ai/p/{encoded_prompt}?width={width}&height={height}&seed={random_seed}&model={model_name}&nologo=true"

    except Exception as e:
        print("Image Engine Error:", str(e))
        return None
