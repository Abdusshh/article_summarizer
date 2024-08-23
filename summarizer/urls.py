from django.urls import path
from .views import summarize_article_view, send_email

urlpatterns = [
    path('summarize', summarize_article_view, name='summarize_article'),
    path('callback', send_email, name='summarization_callback'),  # Callback URL
]
