# Article Summarizer

This project is an article summarizer that allows you to summarize articles using OpenAI's GPT 3.5 LLM.

## Installation

1. Clone the repository:

    ```bash
    git clone <GITHUB LINK>
    ```

2. Navigate to the project directory:

    ```bash
    cd article_summarizer
    ```

3. Create a virtual environment:

    ```bash
    python -m venv venv
    ```

4. Activate the virtual environment:

    - For Windows:

      ```bash
      venv\Scripts\activate
      ```

    - For macOS/Linux:

      ```bash
      source bin/activate
      ```

5. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

6. Set the required environment variables:

    Replace `QSTASH_TOKEN`, `DEPLOYED_URL`, `SENDGRID_API_KEY`, and `SENDGRID_SENDER_EMAIL_ADDRESS` with your own values. 
    
    You can find the `SENDGRID_API_KEY` and `SENDGRID_SENDER_EMAIL_ADDRESS` in your SendGrid account.

    You can find the `QSTASH_TOKEN` in your Upstash account.

    You can leave the `DEPLOYED_URL` blank and set it later when you deploy the application.

## Usage

1. Run the application locally:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://localhost:8000/scheduler/schedule-email`.

3. Follow the instructions on the web page to schedule and send emails.