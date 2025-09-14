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



