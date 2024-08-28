from qstash import QStash
from qstash.chat import openai
from django.conf import settings

client = QStash(settings.QSTASH_TOKEN)

def publish_message_to_openai(article_content, callback_url):
    response = client.message.publish_json(
        api={"name": "llm", "provider": openai(settings.OPENAI_API_KEY)},
        body={
            "model": "gpt-3.5-turbo",
            "messages": [
                {
                    "role": "user",
                    "content": f"Summarize the following article: {article_content} \n in 50-100 words, highlighting the main points and key findings. Please use your own words and avoid copying and pasting from the original text. If the article has multiple sections or parts, focus on the most important and relevant information. Thank you!",
                }
            ],
        },
        callback=callback_url,
        headers={"Retry-After": "60",},
    )
    return response