from django.urls import path
from .views import summarize_article_view, openai_callback_view, get_csrf_token_view

urlpatterns = [
    path('summarize', summarize_article_view, name='summarize_article'),
    path('callback', openai_callback_view, name='summarization_callback'),  # Callback URL
    path('get-csrf-token', get_csrf_token_view, name='get_csrf_token'),
]
