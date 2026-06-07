# Autonomous Customer Support Resolution Agent

An enterprise-grade, zero-touch customer support ecosystem that bridges cloud-based helpdesk platforms with privacy-first, local AI intelligence. This project leverages an event-driven automation workflow to ingest support tickets, perform semantic Retrieval-Augmented Generation (RAG) against corporate policies, execute local Large Language Model (LLM) inference, and trigger deterministic backend system responses.

---

## 🚀 Features

- **Event-Driven Automation:** Real-time ingestion of cloud webhooks routed instantly into a local staging environment.
- **Privacy-First Architecture:** Local semantic vector search and LLM inference ensuring sensitive customer data never leaves private infrastructure.
- **Retrieval-Augmented Generation (RAG):** Contextual policy injection using high-dimensional mathematical vector embeddings to ground AI reasoning.
- **Deterministic Multi-Branch Routing:** Translates unstructured text analysis into strict, structured control flows using an n8n conditional execution matrix.
- **Agentic Function Calling:** Empowering the AI to transition from a conversational chatbot into an operational executor by safely triggering backend microservice APIs.
- **Automated Ticket Lifecycles:** Seamless CRUD operations on helpdesk resources (updating priority states, posting public timeline resolutions, triggering human escalation handoffs).

---

## 🛠️ Tech Stack

| Component | Technology | Role |
| :--- | :--- | :--- |
| **Orchestration** | [n8n](https://n8n.io/) | Visual node-based workflow engine controlling event lifecycles. |
| **Ingress/Proxy** | [ngrok](https://ngrok.com/) | Secure public-to-local reverse proxy tunnel bypassing firewalls. |
| **SaaS Helpdesk** | [Freshdesk](https://freshdesk.com/) | Customer ticketing platform hosting incoming consumer grievances. |
| **Web Framework**| [FastAPI](https://fastapi.tiangolo.com/) | High-performance, asynchronous Python gateway middleware. |
| **Web Server** | [Uvicorn](https://www.uvicorn.org/) | ASGI web server handling network sockets for the FastAPI layer. |
| **Vector DB** | [ChromaDB](https://www.trychroma.com/) | AI-native persistent vector store handling semantic policy retrieval. |
| **LLM Engine** | [Ollama](https://ollama.com/) | Local runtime hosting and serving containerized open-weight models. |
| **Language Model**| [Microsoft Phi-3](https://azure.microsoft.com/en-us/products/phi-3/) | Compact, highly capable 3.8B parameter reasoning model. |

---

## 📁 Project Structure

```text
├── chroma_db/               # Persistent disk storage for ChromaDB vector embeddings
├── setup_kb.py              # Seeding script to build and index the corporate vector knowledge base
├── processor.py             # RAG mechanism, prompt templates, and Ollama API communication loop
├── main.py                  # Core FastAPI application entry point and Uvicorn runtime config
└── n8n_workflow.json        # Exported JSON schema of the node-based automation workflow
