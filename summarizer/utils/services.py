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

import requests


# def publish_to_openai_with_restapi(article_content, callback_url):

# #     # Step 1: Fetch the CSRF token
# #     csrf_token_response = requests.get(f'{settings.DEPLOYMENT_URL}/get-csrf-token')
# #     csrf_token = csrf_token_response.json().get('csrf_token')

# #     # Print the CSRF token for debugging purposes
# #     print(f"Retrieved CSRF Token: {csrf_token}")

# #     headers = {
# #     'Authorization': f'Bearer {settings.QSTASH_TOKEN}',
# #     'Content-Type': 'application/json',
# #     'Upstash-Method': 'POST',
# #     'Upstash-Retries': '3',
# #     'Upstash-Callback-Forward-Referer': 'https://qstash.upstash.io',
# #     'Upstash-Callback-Forward-X-CSRFToken': csrf_token,
# #     'Retry-After': '60',
# #     'Upstash-Callback': callback_url,
# # }

# #     json_data = {"model": "meta-llama/Meta-Llama-3-8B-Instruct", "messages": [{"role": "user", "content": f"Summarize the following article: {article_content} \n in 50-100 words, highlighting the main points and key findings. Please use your own words and avoid copying and pasting from the original text. If the article has multiple sections or parts, focus on the most important and relevant information. Thank you!"}]}

# #     response = requests.post(
# #         'https://qstash.upstash.io/v2/publish/api/llm',
# #         headers=headers,
# #         json=json_data
# #     )

#     client = QStash(settings.QSTASH_TOKEN)
#     print(settings.DEPLOYMENT_URL)
#     response = client.message.publish_json(
#         url=f"{settings.DEPLOYMENT_URL}/callback",
#         # body={"status":200,"header":{"Content-Length":["806"],"Content-Type":["application/json"],"Date":["Mon, 26 Aug 2024 13:39:52 GMT"],"Strict-Transport-Security":["max-age=31536000; includeSubDomains"],"X-Ratelimit-Limit-Requests":["30"],"X-Ratelimit-Limit-Tokens":["1000"],"X-Ratelimit-Remaining-Requests":["30"],"X-Ratelimit-Remaining-Tokens":["1000"],"X-Ratelimit-Reset-Requests":["53s"],"X-Ratelimit-Reset-Tokens":["53s"]},"body":"eyJpZCI6ImNtcGwtODdiY2U3ZjY0ZjdjNDlhOWE4MzhkYWUwMDMyYjdhNzkiLCJvYmplY3QiOiJjaGF0LmNvbXBsZXRpb24iLCJjcmVhdGVkIjoxNzI0Njc5NTkwLCJtb2RlbCI6Im1ldGEtbGxhbWEvTWV0YS1MbGFtYS0zLThCLUluc3RydWN0IiwiY2hvaWNlcyI6W3siaW5kZXgiOjAsIm1lc3NhZ2UiOnsicm9sZSI6ImFzc2lzdGFudCIsImNvbnRlbnQiOiJUaGUgYXJ0aWNsZSBoaWdobGlnaHRzIHRoZSBzaWduaWZpY2FuY2Ugb2YgZm9vZCBiZXlvbmQgbWVyZSBzdXN0ZW5hbmNlLCBlbXBoYXNpemluZyBpdHMgcm9sZSBpbiBicmluZ2luZyBwZW9wbGUgdG9nZXRoZXIsIGV2b2tpbmcgZW1vdGlvbnMsIGFuZCBjcmVhdGluZyBtZW1vcmllcy4gSXQgbm90ZXMgdGhlIGluY3JlZGlibGUgZGl2ZXJzaXR5IG9mIGdsb2JhbCBjdWlzaW5lLCB3aXRoIGVhY2ggcmVnaW9uIGFuZCBjb3VudHJ5IGJvYXN0aW5nIHVuaXF1ZSBmbGF2b3JzLCBpbmdyZWRpZW50cywgYW5kIGNvb2tpbmcgdGVjaG5pcXVlcyB0aGF0IHNldCBpdCBhcGFydC4gRnJvbSBzcGljeSBJbmRpYW4gY3VycmllcyB0byByaWNoIEl0YWxpYW4gcGFzdGEgZGlzaGVzLCB0aGUgYXJvbWFzIGFuZCBmbGF2b3JzIG9mIGdsb2JhbCBjdWlzaW5lIHJlZmxlY3QgdGhlIHJpY2ggdGFwZXN0cnkgb2YgaHVtYW4gZXhwZXJpZW5jZS4ifSwibG9ncHJvYnMiOm51bGwsImZpbmlzaF9yZWFzb24iOiJzdG9wIiwic3RvcF9yZWFzb24iOm51bGx9XSwidXNhZ2UiOnsicHJvbXB0X3Rva2VucyI6MTYzLCJ0b3RhbF90b2tlbnMiOjI0OCwiY29tcGxldGlvbl90b2tlbnMiOjg1fX0=","sourceMessageId":"msg_26hZCxZCuWyyTWPmSVBrNC1RACuGc47NLFnLK2JoV5UiuoCV99cXHhd1Je7LF3j","url":"https://qstash.upstash.io/llm/v1/chat/completions","method":"POST","sourceHeader":{"Content-Type":["application/json"]},"sourceBody":"eyJtb2RlbCI6ICJtZXRhLWxsYW1hL01ldGEtTGxhbWEtMy04Qi1JbnN0cnVjdCIsICJtZXNzYWdlcyI6IFt7InJvbGUiOiAidXNlciIsICJjb250ZW50IjogIlN1bW1hcml6ZSB0aGUgZm9sbG93aW5nIGFydGljbGU6IEZvb2QgaXMgbW9yZSB0aGFuIGp1c3QgYSBuZWNlc3NpdHkgZm9yIHN1cnZpdmFsOyBpdCdzIGEgdW5pdmVyc2FsIGxhbmd1YWdlIHRoYXQgYnJpbmdzIHBlb3BsZSB0b2dldGhlciwgZXZva2VzIGVtb3Rpb25zLCBhbmQgY3JlYXRlcyBtZW1vcmllcy4gV2l0aCB0aGUgd29ybGQncyBjdWxpbmFyeSBsYW5kc2NhcGUgYXMgZGl2ZXJzZSBhcyBpdHMgY3VsdHVyZXMsIGV2ZXJ5IHJlZ2lvbiBhbmQgY291bnRyeSBoYXMgaXRzIG93biB1bmlxdWUgZmxhdm9ycywgaW5ncmVkaWVudHMsIGFuZCBjb29raW5nIHRlY2huaXF1ZXMgdGhhdCBzZXQgaXRzIGN1aXNpbmUgYXBhcnQuIEZyb20gc3BpY3kgY3VycmllcyBvZiBJbmRpYSB0byByaWNoIHBhc3RhIGRpc2hlcyBvZiBJdGFseSwgdGhlIGFyb21hcyBhbmQgZmxhdm9ycyBvZiBnbG9iYWwgY3Vpc2luZSBhcmUgYSB0cnVlIHJlZmxlY3Rpb24gb2YgdGhlIGRpdmVyc2l0eSBvZiBodW1hbiBleHBlcmllbmNlLlxyXG4gXG4gaW4gNTAtMTAwIHdvcmRzLCBoaWdobGlnaHRpbmcgdGhlIG1haW4gcG9pbnRzIGFuZCBrZXkgZmluZGluZ3MuIFBsZWFzZSB1c2UgeW91ciBvd24gd29yZHMgYW5kIGF2b2lkIGNvcHlpbmcgYW5kIHBhc3RpbmcgZnJvbSB0aGUgb3JpZ2luYWwgdGV4dC4gSWYgdGhlIGFydGljbGUgaGFzIG11bHRpcGxlIHNlY3Rpb25zIG9yIHBhcnRzLCBmb2N1cyBvbiB0aGUgbW9zdCBpbXBvcnRhbnQgYW5kIHJlbGV2YW50IGluZm9ybWF0aW9uLiBUaGFuayB5b3UhIn1dfQ==","maxRetries":3,"notBefore":1724679589965,"createdAt":1724679589965,"callerIP":"31.141.39.67","api":"llm"},
#         body = {
#             'to_email': 'abdullah.enes.gules@gmail.com',
#             'subject': 'subject',
#             'content': 'content',
#             'body': 'eyJpZCI6ImNtcGwtODdiY2U3ZjY0ZjdjNDlhOWE4MzhkYWUwMDMyYjdhNzkiLCJvYmplY3QiOiJjaGF0LmNvbXBsZXRpb24iLCJjcmVhdGVkIjoxNzI0Njc5NTkwLCJtb2RlbCI6Im1ldGEtbGxhbWEvTWV0YS1MbGFtYS0zLThCLUluc3RydWN0IiwiY2hvaWNlcyI6W3siaW5kZXgiOjAsIm1lc3NhZ2UiOnsicm9sZSI6ImFzc2lzdGFudCIsImNvbnRlbnQiOiJUaGUgYXJ0aWNsZSBoaWdobGlnaHRzIHRoZSBzaWduaWZpY2FuY2Ugb2YgZm9vZCBiZXlvbmQgbWVyZSBzdXN0ZW5hbmNlLCBlbXBoYXNpemluZyBpdHMgcm9sZSBpbiBicmluZ2luZyBwZW9wbGUgdG9nZXRoZXIsIGV2b2tpbmcgZW1vdGlvbnMsIGFuZCBjcmVhdGluZyBtZW1vcmllcy4gSXQgbm90ZXMgdGhlIGluY3JlZGlibGUgZGl2ZXJzaXR5IG9mIGdsb2JhbCBjdWlzaW5lLCB3aXRoIGVhY2ggcmVnaW9uIGFuZCBjb3VudHJ5IGJvYXN0aW5nIHVuaXF1ZSBmbGF2b3JzLCBpbmdyZWRpZW50cywgYW5kIGNvb2tpbmcgdGVjaG5pcXVlcyB0aGF0IHNldCBpdCBhcGFydC4gRnJvbSBzcGljeSBJbmRpYW4gY3VycmllcyB0byByaWNoIEl0YWxpYW4gcGFzdGEgZGlzaGVzLCB0aGUgYXJvbWFzIGFuZCBmbGF2b3JzIG9mIGdsb2JhbCBjdWlzaW5lIHJlZmxlY3QgdGhlIHJpY2ggdGFwZXN0cnkgb2YgaHVtYW4gZXhwZXJpZW5jZS4ifSwibG9ncHJvYnMiOm51bGwsImZpbmlzaF9yZWFzb24iOiJzdG9wIiwic3RvcF9yZWFzb24iOm51bGx9XSwidXNhZ2UiOnsicHJvbXB0X3Rva2VucyI6MTYzLCJ0b3RhbF90b2tlbnMiOjI0OCwiY29tcGxldGlvbl90b2tlbnMiOjg1fX0='
#         }
#     )

#     return response


# from qstash import QStash
# from qstash.chat import upstash
# def completion_with_meta_llama(article_content, callback_url):

#     client = QStash(settings.QSTASH_TOKEN)

#     # completion = client.chat.create(
#     #     provider=upstash(),
#     #     model="meta-llama/Meta-Llama-3-8B-Instruct",
#     #     messages=[
#     #         {
#     #             "role": "user",
#     #             "content": "What is a large language model?",
#     #         },
#     #     ],
#     # )

#     # print(completion)

#     # First, get the CSRF token
#     session = requests.Session()
#     print(callback_url)
#     response = session.get(callback_url)
#     print(response.cookies)
#     csrf_token = session.cookies.get('csrftoken')
#     print(csrf_token)

#     client.message.publish_json(
#         url=callback_url,
#         body={"status":200,"header":{"Content-Length":["806"],"Content-Type":["application/json"],"Date":["Mon, 26 Aug 2024 13:39:52 GMT"],"Strict-Transport-Security":["max-age=31536000; includeSubDomains"],"X-Ratelimit-Limit-Requests":["30"],"X-Ratelimit-Limit-Tokens":["1000"],"X-Ratelimit-Remaining-Requests":["30"],"X-Ratelimit-Remaining-Tokens":["1000"],"X-Ratelimit-Reset-Requests":["53s"],"X-Ratelimit-Reset-Tokens":["53s"]},"body":"eyJpZCI6ImNtcGwtODdiY2U3ZjY0ZjdjNDlhOWE4MzhkYWUwMDMyYjdhNzkiLCJvYmplY3QiOiJjaGF0LmNvbXBsZXRpb24iLCJjcmVhdGVkIjoxNzI0Njc5NTkwLCJtb2RlbCI6Im1ldGEtbGxhbWEvTWV0YS1MbGFtYS0zLThCLUluc3RydWN0IiwiY2hvaWNlcyI6W3siaW5kZXgiOjAsIm1lc3NhZ2UiOnsicm9sZSI6ImFzc2lzdGFudCIsImNvbnRlbnQiOiJUaGUgYXJ0aWNsZSBoaWdobGlnaHRzIHRoZSBzaWduaWZpY2FuY2Ugb2YgZm9vZCBiZXlvbmQgbWVyZSBzdXN0ZW5hbmNlLCBlbXBoYXNpemluZyBpdHMgcm9sZSBpbiBicmluZ2luZyBwZW9wbGUgdG9nZXRoZXIsIGV2b2tpbmcgZW1vdGlvbnMsIGFuZCBjcmVhdGluZyBtZW1vcmllcy4gSXQgbm90ZXMgdGhlIGluY3JlZGlibGUgZGl2ZXJzaXR5IG9mIGdsb2JhbCBjdWlzaW5lLCB3aXRoIGVhY2ggcmVnaW9uIGFuZCBjb3VudHJ5IGJvYXN0aW5nIHVuaXF1ZSBmbGF2b3JzLCBpbmdyZWRpZW50cywgYW5kIGNvb2tpbmcgdGVjaG5pcXVlcyB0aGF0IHNldCBpdCBhcGFydC4gRnJvbSBzcGljeSBJbmRpYW4gY3VycmllcyB0byByaWNoIEl0YWxpYW4gcGFzdGEgZGlzaGVzLCB0aGUgYXJvbWFzIGFuZCBmbGF2b3JzIG9mIGdsb2JhbCBjdWlzaW5lIHJlZmxlY3QgdGhlIHJpY2ggdGFwZXN0cnkgb2YgaHVtYW4gZXhwZXJpZW5jZS4ifSwibG9ncHJvYnMiOm51bGwsImZpbmlzaF9yZWFzb24iOiJzdG9wIiwic3RvcF9yZWFzb24iOm51bGx9XSwidXNhZ2UiOnsicHJvbXB0X3Rva2VucyI6MTYzLCJ0b3RhbF90b2tlbnMiOjI0OCwiY29tcGxldGlvbl90b2tlbnMiOjg1fX0=","sourceMessageId":"msg_26hZCxZCuWyyTWPmSVBrNC1RACuGc47NLFnLK2JoV5UiuoCV99cXHhd1Je7LF3j","url":"https://qstash.upstash.io/llm/v1/chat/completions","method":"POST","sourceHeader":{"Content-Type":["application/json"]},"sourceBody":"eyJtb2RlbCI6ICJtZXRhLWxsYW1hL01ldGEtTGxhbWEtMy04Qi1JbnN0cnVjdCIsICJtZXNzYWdlcyI6IFt7InJvbGUiOiAidXNlciIsICJjb250ZW50IjogIlN1bW1hcml6ZSB0aGUgZm9sbG93aW5nIGFydGljbGU6IEZvb2QgaXMgbW9yZSB0aGFuIGp1c3QgYSBuZWNlc3NpdHkgZm9yIHN1cnZpdmFsOyBpdCdzIGEgdW5pdmVyc2FsIGxhbmd1YWdlIHRoYXQgYnJpbmdzIHBlb3BsZSB0b2dldGhlciwgZXZva2VzIGVtb3Rpb25zLCBhbmQgY3JlYXRlcyBtZW1vcmllcy4gV2l0aCB0aGUgd29ybGQncyBjdWxpbmFyeSBsYW5kc2NhcGUgYXMgZGl2ZXJzZSBhcyBpdHMgY3VsdHVyZXMsIGV2ZXJ5IHJlZ2lvbiBhbmQgY291bnRyeSBoYXMgaXRzIG93biB1bmlxdWUgZmxhdm9ycywgaW5ncmVkaWVudHMsIGFuZCBjb29raW5nIHRlY2huaXF1ZXMgdGhhdCBzZXQgaXRzIGN1aXNpbmUgYXBhcnQuIEZyb20gc3BpY3kgY3VycmllcyBvZiBJbmRpYSB0byByaWNoIHBhc3RhIGRpc2hlcyBvZiBJdGFseSwgdGhlIGFyb21hcyBhbmQgZmxhdm9ycyBvZiBnbG9iYWwgY3Vpc2luZSBhcmUgYSB0cnVlIHJlZmxlY3Rpb24gb2YgdGhlIGRpdmVyc2l0eSBvZiBodW1hbiBleHBlcmllbmNlLlxyXG4gXG4gaW4gNTAtMTAwIHdvcmRzLCBoaWdobGlnaHRpbmcgdGhlIG1haW4gcG9pbnRzIGFuZCBrZXkgZmluZGluZ3MuIFBsZWFzZSB1c2UgeW91ciBvd24gd29yZHMgYW5kIGF2b2lkIGNvcHlpbmcgYW5kIHBhc3RpbmcgZnJvbSB0aGUgb3JpZ2luYWwgdGV4dC4gSWYgdGhlIGFydGljbGUgaGFzIG11bHRpcGxlIHNlY3Rpb25zIG9yIHBhcnRzLCBmb2N1cyBvbiB0aGUgbW9zdCBpbXBvcnRhbnQgYW5kIHJlbGV2YW50IGluZm9ybWF0aW9uLiBUaGFuayB5b3UhIn1dfQ==","maxRetries":3,"notBefore":1724679589965,"createdAt":1724679589965,"callerIP":"31.141.39.67","api":"llm"},
#         headers={"Retry-After": "60",
#                  "Referer": "https://qstash.upstash.io",
#                  "X-CSRFToken": csrf_token},
#     )