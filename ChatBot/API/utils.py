import openai
from django.conf import settings

openai.api_key = settings.APIKEY

def send_code_to_api(code):
    try:
        res = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system","content": "You are an experienced Fitness Expert."},
                {"role": "user","content": f"You are a knowledgeable and empathetic Fitness Expert, dedicated to providing guidance, support, and motivation for users on various fitness, exercise, nutrition, and mental health topics in a safe and non-judgmental environment. Your responses are informative, encouraging, and tailored to users' specific needs, offering actionable steps and additional resources as needed: {code}"},
            ]
        )        
        return res["choices"][0]["message"]["content"]

    except Exception as e:
        print(f"Error: {e}")
        return "Sorry, an error occurred while processing your request."
