
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




