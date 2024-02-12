import requests
import json
from PIL import Image
import io
from transformers import ViTFeatureExtractor, ViTForImageClassification

def generate_image(input_text_generation):
    url =  "https://stablediffusionapi.com/api/v4/dreambooth"
    payload = json.dumps({
            "key":  "svPEQzcNyeGD4exr4dC9Jk0rITbCIkFKLehPF6vGalnm6f2yjlMjAudbzRch",  
            "model_id":  "juggernaut-xl-v5",  
            "prompt":  input_text_generation,  
            "negative_prompt":  "painting, extra fingers, mutated hands, poorly drawn hands, poorly drawn face, deformed, ugly, blurry, bad anatomy, bad proportions, extra limbs, cloned face, skinny, glitchy, double torso, extra arms, extra hands, mangled fingers, missing lips, ugly face, distorted face, extra legs, anime",  
            "width":  "512",  
            "height":  "512",  
            "samples":  "1",  
            "num_inference_steps":  "30",  
            "safety_checker":  "no",  
            "enhance_prompt":  "yes",  
            "seed":  None,  
            "guidance_scale":  7.5,  
            "multi_lingual":  "no",  
            "panorama":  "no",  
            "self_attention":  "no",  
            "upscale":  "no",  
            "embeddings":  "embeddings_model_id",  
            "lora":  "lora_model_id",  
            "webhook":  None,  
            "track_id":  None  
    })

    headers = {
        'Content-Type': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    image_link = response.json()['output'][0]
    return image_link

def classify_image(uploaded_file):
    try:
        contents = uploaded_file.read()
        image = Image.open(io.BytesIO(contents))
        feature_extractor = ViTFeatureExtractor.from_pretrained('google/vit-base-patch16-224')
        model = ViTForImageClassification.from_pretrained('google/vit-base-patch16-224')
        inputs = feature_extractor(images=image, return_tensors="pt")
        outputs = model(**inputs)
        logits = outputs.logits
        predicted_class_idx = logits.argmax(-1).item()
        predicted_class = model.config.id2label[predicted_class_idx]
        return predicted_class
    except Exception as e:
        return f"Ocurrió un error: {str(e)}"
