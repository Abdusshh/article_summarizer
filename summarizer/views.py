import base64
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .utils.services import publish_message_to_openai
from .utils.email_services import send_email
from django.conf import settings

@csrf_exempt
def openai_callback_view(request):
    if request.method == 'POST':
        # Parse the request body
        data = json.loads(request.body)

        # Decode the base64-encoded 'body' field from the callback
        encoded_body = data.get('body', '')
        decoded_body = base64.b64decode(encoded_body).decode('utf-8')

        # Parse the decoded body to JSON format
        decoded_data = json.loads(decoded_body)

        # Extract the summary from the decoded OpenAI response
        summary = decoded_data['choices'][0]['message']['content']

        # Extract the email and subject from the query parameters
        to_email = request.GET.get('to_email')
        subject = request.GET.get('subject')

        # Send the summary via email
        response = send_email(to_email, subject, summary)


        return JsonResponse({'status': 'Email sent', 'response': response.status_code})
    
    return JsonResponse({'error': 'Invalid request'}, status=400)

@csrf_exempt
def summarize_article_view(request):
    if request.method == 'POST':
        # Handle form submission
        to_email = request.POST.get('to_email')
        subject = request.POST.get('subject')
        article_content = request.POST.get('content')

        # Define your callback URL, passing necessary email details to the callback
        callback_url = f'{settings.DEPLOYMENT_URL}/callback?to_email={to_email}&subject={subject}'

        # Publish to QStash/OpenAI
        response = publish_message_to_openai(article_content, callback_url)

        print(response)

        if response:
            return render(request, 'summarizer/index.html', {'email_scheduled': True})
        else:
            return render(request, 'summarizer/index.html', {'error': 'Failed to send summary.'})
    
    # If GET request, render the form
    return render(request, 'summarizer/index.html')
