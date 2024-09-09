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

    Replace `OPENAI_API_KEY`, `QSTASH_TOKEN`, `DEPLOYMENT_URL`, `UPSTASH_REDIS_REST_URL`, and `UPSTASH_REDIS_REST_TOKEN` with your own values.

    You can find the `OPENAI_API_KEY` in your OpenAI account.

    You can find the `QSTASH_TOKEN`, `UPSTASH_REDIS_REST_URL`, and `UPSTASH_REDIS_REST_TOKEN` in your Upstash account.

    You can leave the `DEPLOYMENT_URL` blank and set it later when you deploy the application.

## Usage

1. Run the application locally:

    ```bash
    python manage.py runserver
    ```

2. Open your web browser and navigate to `http://localhost:8000/summarizer/summarize`.

3. Fill in the form with mail address, mail subject, and article text that you want to summarize.

4. Click the "Summarize" button to get the summary mailed to you.
