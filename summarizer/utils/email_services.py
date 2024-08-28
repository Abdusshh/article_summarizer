import requests

def send_email(to_email, subject, content):
    url = 'https://email-scheduler-dun.vercel.app/scheduler/send-email'
    payload = {
        'to_email': to_email,
        'subject': subject,
        'content': content,
    }
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response

# test the function
if __name__ == '__main__':
    to_email = 'abdullah.enes189@gmail.com'
    subject = 'Test Email'
    content = 'This is a test email sent from Python.'
    response = send_email(to_email, subject, content)
    print(response)