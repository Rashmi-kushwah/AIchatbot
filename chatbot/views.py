# import openai
# from django.http import JsonResponse
# from django.shortcuts import render
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()
# openai.api_key = os.getenv("OPENAI_API_KEY")  

# # Chat history store karne ke liye ek dictionary (User-wise store karna ho to session ya database use kar sakte ho)
# chat_history = []

# def chatbot_response(request):
#     if request.method == "POST":
#         user_message = request.POST.get("message")

#         # User ke message ko chat history me add karna
#         chat_history.append({"role": "user", "content": user_message})

#         # OpenAI API se response lena
#         response = openai.ChatCompletion.create(
#             model="gpt-3.5-turbo",
#             messages=chat_history
#         )

#         # Chatbot ka reply lena
#         bot_reply = response["choices"][0]["message"]["content"]

#         # Bot ke reply ko bhi history me add karna
#         chat_history.append({"role": "assistant", "content": bot_reply})

#         return JsonResponse({"reply": bot_reply})
    
#     return render(request, "chat.html")





# Cohere Api 


import cohere
import json
from django.conf import settings
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token

# Cohere API Key Set Karna
COHERE_API_KEY = "xo7v6owa6LrUPQjVq1zam7QpElelAR8NL3S4GFR8"
co = cohere.Client(COHERE_API_KEY)

# Chat Page Render Karega
def chatbot_page(request):
    return render(request, "chat.html")

# CSRF Token Generate Karega
def get_csrf_token(request):
    token = get_token(request)
    return JsonResponse({"csrfToken": token})

# Chatbot Response API
@csrf_exempt
def chatbot_response(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            user_message = data.get("message", "")

            if not user_message:
                return JsonResponse({"error": "Message is required"}, status=400)

            # Cohere AI API Call
            response = co.generate(
                model="command",
                prompt=user_message,
                max_tokens=50
            )

            bot_reply = response.generations[0].text
            return JsonResponse({"response": bot_reply})

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)




# Gemini Api key








# from django.shortcuts import render
# # # Chat Page Render Karega
# def chatbot_page(request):
#     return render(request, "chat.html")

# # # CSRF Token Generate Karega
# def get_csrf_token(request):
#     token = get_token(request)
#     return JsonResponse({"csrfToken": token})


# import requests
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings  # Ensure API Key is in settings.py
# from django.middleware.csrf import get_token
# from django.middleware.csrf import get_token

# import requests
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings  
# from django.middleware.csrf import get_token
# import requests
# import json
# from django.http import JsonResponse
# from django.views.decorators.csrf import csrf_exempt
# from django.conf import settings  
# from django.middleware.csrf import get_token

# print("Google API Key:", settings.GOOGLE_API_KEY)

# @csrf_exempt
# def chatbot_response(request):
#     if request.method == "POST":
#         try:
#             data = json.loads(request.body)
#             user_message = data.get("message", "")

#             if not user_message:
#                 return JsonResponse({"error": "Message is required"}, status=400)

#             url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateText"
#             headers = {"Content-Type": "application/json"}

#             # ✅ Correct Payload Format
#             payload = {
#                 "contents": [
#                     {
#                         "role": "user",
#                         "parts": [{"text": user_message}]
#                     }
#                 ],
#                 "temperature": 0.7,
#                 "maxOutputTokens": 100
#             }

#             params = {"key": settings.GOOGLE_API_KEY}

#             response = requests.post(url, headers=headers, params=params, json=payload, timeout=10)

#             print("API Status Code:", response.status_code)
#             print("API Response:", response.text)  # Debugging Response

#             if response.status_code == 200:
#                 response_json = response.json()
#                 bot_reply = response_json.get("candidates", [{}])[0].get("content", "No response")
#                 return JsonResponse({"response": bot_reply})
#             else:
#                 return JsonResponse({"error": f"Failed to get response, status: {response.status_code}, message: {response.text}"}, status=500)

#         except Exception as e:
#             return JsonResponse({"error": str(e)}, status=500)

#     return JsonResponse({"error": "Invalid request"}, status=400)
