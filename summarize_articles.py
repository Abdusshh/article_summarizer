# We have 1000 articles that we want to summarize
# We will summarize these articles using qstash queues
from upstash_redis import Redis
from qstash import QStash
from qstash.chat import upstash
from dotenv import load_dotenv
import os

load_dotenv()
redis = Redis.from_env()
qstash_client = QStash(os.getenv("QSTASH_TOKEN"))

qstash_client.queue.upsert("articles-queue", parallelism=2)

for i in range(1, 1001):

    article = redis.get(f"article_{i}")

    result = qstash_client.message.enqueue_json(
        queue="articles-queue",
        api={"name": "llm", "provider": upstash()},
        body={
            "model": "meta-llama/Meta-Llama-3-8B-Instruct",
            "messages": [
                {
                    "role": "user",
                    "content": f"Summarize the following article: {article} \n in 50-100 words, highlighting the main points and key findings. Please use your own words and avoid copying and pasting from the original text. If the article has multiple sections or parts, focus on the most important and relevant information. Thank you!",
                }
            ],
        },
        callback=f'{os.getenv("DEPLOYMENT_URL")}/redis-callback?article_id={i}',
    )

print(result)
