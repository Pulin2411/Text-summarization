<img width="1024" height="682" alt="image" src="https://github.com/user-attachments/assets/8a8d6a63-e1f2-4de4-b6a3-b125156d0907" /># 📝 FastAPI Text Summarization API (Gemini-1.5)

This project is a simple yet powerful **text summarization API** built using [FastAPI](https://fastapi.tiangolo.com/), powered by **Google Gemini-1.5**.  
It allows users to submit text and receive a summarized version (short, medium, or detailed).

---

## 🚀 Features

- **REST API** built with FastAPI – lightweight & production-ready.
- **Google Gemini-1.5** integration for accurate summarization.
- **Customizable summaries** – choose between `short`, `medium`, and `detailed` outputs.
- Easy to deploy with `uvicorn`.

---

## 🛠️ Project Structure

| Component     | Technology Used   |
| ------------- | ----------------- |
| API Framework | FastAPI           |
| AI Model      | Google Gemini-1.5 |
| HTTP Client   | Requests          |
| Server        | Uvicorn           |

---

## 🖼 Technical Diagram

Here’s a simple but professional architecture diagram:

- **Client (Postman, Frontend, CLI)** → sends POST request with text  
- **FastAPI (app.py)** → receives request → builds prompt → calls Gemini API  
- **Gemini API (Google AI)** → returns summarized text  
- **FastAPI Response** → returns summarized result as JSON  


---

## 🖼 Technical Diagram

Here’s a simple but professional architecture diagram:

- **Client (Postman, Frontend, CLI)** → sends POST request with text  
- **FastAPI (app.py)** → receives request → builds prompt → calls Gemini API  
- **Gemini API (Google AI)** → returns summarized text  
- **FastAPI Response** → returns summarized result as JSON  

### About Author
Pulin Shah — Lead IT Support Coordinator | IT Service Delivery | n8n Automations |ML|DL|Data Science|Prompt Enigneering|RAG|Gen-AI|EDA

IT service delivery leader with 20+ years across incident, change, and problem management, PSA/RMM operations (ConnectWise), and endpoint security. Designs and operates Service Desk workflows with SLA rigor, and builds support automations using n8n, LLMs, and vector search for policy-aligned responses.

Leads Service Desk operations: ticket triage, scheduling, vendor coordination, SLA governance, and reporting.

Builds LLM-powered assistants on Telegram with strict topic guardrails and end-of-conversation flows.

Implements RAG pipelines: Google Drive ingestion, OpenAI embeddings (512-dim), Pinecone indexing, and chunking strategies for retrieval quality.

Experienced with ESET/SentinelOne endpoints, Microsoft stack, AWS (Solutions Architect), and ITIL-based practices for change/incident/request management.

Links

GitHub: https://github.com/Pulin2411

LinkedIn: linkedin.com/in/pulin-shah-741212b

Email: pulin2411@gmail.com

