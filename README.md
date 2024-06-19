# LemurAI - LLM Module

LemurAI is a conversational AI developed using the LangChain library tailored to assist at Acecom events. This service uses a language model to answer queries dynamically, providing a personalized interaction based on historical conversation context.

## Project Structure

- `lemur_core.py`: Core functionalities including model initialization and query handling.
- `lemur_service.py`: FastAPI service that exposes the model as an API for receiving queries and sending responses.
- `lemur_test_llm_service.py`: A test script for sending requests to the FastAPI service.
- `.env`: Environment file for storing sensitive keys (like the API key).
- `requirements.txt`: Python dependencies required for the project.
- `Acecom_IA___Proyecto_Feria_UNI_2024.pdf`: Document used as reference material for the AI responses.
- `README.md`: Documentation to help navigate and utilize the repository.

## Setup Instructions

### Requirements

- Python 3.8+
- pip

### Installation

1. Clone the repository to your local machine.
2. Navigate to the repository directory:

   ```bash
   cd path_to_repository
   ```

3. Install the required Python packages:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up your `.env` file with the necessary API keys:

   ```plaintext
   GROQ_API_KEY=your_api_key_here
   ```

### Running the Service

To run the FastAPI server:

```bash
uvicorn lemur_service:app --reload
```

The server will start on `http://127.0.0.1:8000` by default. The API documentation will be available at `http://127.0.0.1:8000/docs`.

## Interacting with the API

You can interact with the API using any HTTP client. The primary endpoint is:

- POST `/query/`: Accepts JSON payloads with a `usuario` key.

### Example Request

Using `curl`:

```bash
curl -X POST 'http://127.0.0.1:8000/query/' \
     -H 'Content-Type: application/json' \
     -d '{"usuario": "Andre"}'
```

Using Python `requests`:

```python
import requests

response = requests.post(
    'http://127.0.0.1:8000/query/',
    json={"usuario": "Alejandro"}
)
print(response.json())
```


## Contact Information

For help or further information, please [contact me](mailto:apachecotaboada@gmail.com).
