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


from django.middleware.csrf import get_token
from django.http import JsonResponse

def get_csrf_token_view(request):
    # This will ensure that the token is set for the session
    csrf_token = get_token(request)
    return JsonResponse({"csrf_token": csrf_token})


# def submit_article(request):
#     if request.method == 'POST':
#         form = ArticleForm(request.POST)
#         if form.is_valid():
#             article = form.save()
#             article.content = form.cleaned_data['content']
#             article.title = form.cleaned_data['title']
#             article.created_at = time.strftime('%Y-%m-%d %H:%M:%S')
#             summarize_article(article)
#             return redirect('article_detail', pk=article.pk)
#     else:
#         form = ArticleForm()
#     return render(request, 'summarizer/submit_article.html', {'form': form})

# def article_detail(request, pk):
#     article = Article.objects.get(pk=pk)
#     return render(request, 'summarizer/article_detail.html', {'article': article})

# def summarize_article(article):
#     client = QStash(settings.QSTASH_TOKEN)

#     article_id = Article.objects.count()  # Get the ID of the article

#     response = client.message.publish_json(
#         api={"name": "llm", "provider": openai(settings.OPENAI_API_KEY)},
#         body={
#             "model": "gpt-3.5-turbo",
#             "messages": [
#                 {
#                     "role": "user",
#                     "content": f"Article ID: {article_id}\n\nSummarize this article: \n {article.content} \n in 50-100 words, highlighting the main points and key findings. Please use your own words and avoid copying and pasting from the original text. If the article has multiple sections or parts, focus on the most important and relevant information. Make sure to start with Article ID: {article_id} for reference.",
#                 }
#             ],
#         },
#         callback="https://firstqstashmessage.requestcatcher.com/", # Replace with your own callback URL when deployed
#         headers={"Retry-After": "60"}, # Retry after 60 seconds if publishing fails due to rate limiting
#     )

#     print(f"Total number of articles: {article_id}")
#     article_title = Article.objects.get(pk=article_id).title
#     print(f"Article title: {article_title}")
#     print(f"message id: {response.message_id}")

# @csrf_exempt
# def summarization_callback(request):
#     if request.method == 'POST':
#         # Decode the base64 encoded body
#         encoded_body = json.loads(request.body).get('body')
#         decoded_body = base64.b64decode(encoded_body).decode('utf-8')
        
#          # Parse the decoded JSON
#         data = json.loads(decoded_body)
#         summary = data.get('choices')[0].get('message').get('content')
        
#         # Extract the article_id from the summary content
#         article_id = int(summary.split("\n")[0].replace("Article ID: ", ""))
#         summary_content = "\n".join(summary.split("\n")[2:])  # Get the actual summary content

#         # Fetch the article and update the summary
#         article = Article.objects.get(pk=article_id)
#         article.summary = summary_content
#         article.save()

#         return JsonResponse({'status': 'success'})
#     return JsonResponse({'status': 'failed'}, status=400)

