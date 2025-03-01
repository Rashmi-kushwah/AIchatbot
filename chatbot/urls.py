# from django.urls import path
# # from .views import chatbot_response
# from django.conf import settings
# from django.conf.urls.static import static
# urlpatterns = [
#     # path('', chatbot_response, name="chatbot"),
# ]
# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




# from django.urls import path
# from .views import chatbot_page, chatbot_response
# from .views import get_csrf_token
# urlpatterns = [
#     path("chatbot/", chatbot_page, name="chatbot_page"),
#     path("chatbot-response/", chatbot_response, name="chatbot_response"),
#     path("get-csrf-token/", get_csrf_token, name="get_csrf_token"),  # CSRF Token URL
# ]


# from django.urls import path
# from .views import chatbot_page, chatbot_response, get_csrf_token

# urlpatterns = [
#     path("chatbot/", chatbot_page, name="chatbot_page"),
#     path("chatbot-response/", chatbot_response, name="chatbot_response"),
#     path("get-csrf-token/", get_csrf_token, name="get_csrf_token"),
# ]

# Gemini 

from django.urls import path
from .views import chatbot_response,get_csrf_token,chatbot_page

urlpatterns = [
    path("chatbot-response/", chatbot_response, name="chatbot_response"),
    path("get-csrf-token/", get_csrf_token, name="get_csrf_token"),
    path("chatbot/", chatbot_page, name="chatbot_page"),
]
