from django.urls import path
from .views import summarize_article_view, openai_callback_view, redis_callback_view

urlpatterns = [
    path('summarize', summarize_article_view, name='summarize_article'),
    path('callback', openai_callback_view, name='summarization_callback'),  # Callback URL for mails
    path('redis-callback', redis_callback_view, name='redis_callback'),  # Callback URL for Redis
]
