# local-llm-fastapi
Local LLM backend service using Ollama (LLaMA 3.1) and FastAPI with structured JSON responses.

This project runs an LLM locally using Ollama and exposes it through a FastAPI backend. The API returns structured JSON responses suitable for other services.

How to run (local machine)

Install Ollama and pull the model:
ollama pull llama3.1

Install Python dependencies:
pip install -r requirements.txt

Start the API:
uvicorn step4_fastapi_llm:app --reload

Open Swagger UI:
http://127.0.0.1:8000/docs

Test:
POST /ask
{"question":"what is a loop"}
