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

```

---

## ⚙️ Setup Instructions (Local)

### 1. Prerequisites
Ensure you have the following installed on your machine:
- Python 3.10+
- Node.js & npm (or the n8n Desktop app)
- Ollama CLI

### 2. Configure Local AI Models
Download and spin up the Microsoft Phi-3 model inside your local Ollama instance:
```bash
ollama run phi3

```

### 3. Clone and Install Python Backend
Navigate to your project directory, set up a virtual environment, and install dependencies:
```bash
pip install fastapi uvicorn requests chromadb

```

### 4. Initialize the Vector Knowledge Base
Run the seeding script to compile corporate policies into mathematical vectors on your disk:
```bash
python setup_kb.py

```

### 5. Start the FastAPI Middleware Gateway
Launch the high-performance local server instance bound to port `8000`:
```bash
python main.py

```

### 6. Establish Exposing Tunnel Networks
In a separate terminal, initialize your ngrok reverse-proxy tunnel to route internet traffic directly to your local n8n instance (default port `5678`):
```bash
ngrok http 5678

```

### 7. Configure n8n & Freshdesk Webhooks
1. Boot up **n8n** and import your `n8n_workflow.json` blueprint canvas.
2. Open the **Webhook** trigger node and copy the custom URL path.
3. Replace the `localhost:5678` segment of the path with your active **ngrok public URL**.
4. Log into your **Freshdesk Admin Console**, navigate to *Automations > Ticket Creation*, and configure a rule to trigger a **Webhook** pointing to that ngrok endpoint whenever a new ticket is generated.

---

## 🔄 How It Works

```text
[Freshdesk Ticket] ──> [ngrok Public Tunnel] ──> [n8n Webhook Node]
                                                          │
                                                (HTTP POST Payload)
                                                          ▼
[n8n Switch Node] <── (JSON Response) <── [FastAPI Gateway (main.py)]
        │                                                 │
        ├── Rule 0 (Auto-Reply) ──> Freshdesk Reply       ├── Query ChromaDB Store
        ├── Rule 1 (Escalate)   ──> Freshdesk PUT (Urgent)├── Build Context Prompt
        └── Rule 2 (Exec Tool)  ──> Mock Backend API      └── Infer via Ollama (Phi-3)

```

---

## 💡 Example Use Cases

### 🔹 Use Case 1: Password Reset Management (Agentic Function Calling)
- **User Query:** *"I can't get into my account, please reset my password."*
- **RAG Ingestion:** Fetches *Password Reset Policy* confirming administrative link authorization.
- **AI Decision Object:** `{"intent": "password_reset", "action": "execute_tool", "tool_command": "send_password_link"}`
- **System Execution:** n8n hits the Mock Backend API with the client's ID, executes the database linkage script, and replies with a confirmation notice.

### 🔹 Use Case 2: Digital Software Refund Request (Policy Enforcement Denial)
- **User Query:** *"I bought your download software yesterday but I don't want it anymore, refund me."*
- **RAG Ingestion:** Retrieves *Refund Policy* stating: *"Digital software products are strictly non-refundable."*
- **AI Decision Object:** `{"intent": "refund", "action": "auto_reply", "draft_response": "..."}`
- **System Execution:** The workflow bypasses human queues, closes the ticket, and posts a polite explanation of corporate software rules to the timeline.

### 🔹 Use Case 3: Identity Theft / Fraud Detection (SLA Escalation)
- **User Query:** *"There's a charge on my credit card from you guys that I never authorized!"*
- **RAG Ingestion:** Pulls *Fraud Protocol* demanding immediate billing team intervention and lock downs.
- **AI Decision Object:** `{"intent": "fraud", "action": "escalate"}`
- **System Execution:** The workflow fires a state update mutating ticket priority to **Urgent**, bypasses auto-replies, alerts internal security managers, and logs a reassurance message to the client.

---

## ⚠️ Limitations

- **Hardware Latency Constraints:** Executing machine learning inference locally relies heavily on host CPU/GPU processing capabilities, causing noticeable variance in ticket throughput times.
- **Ephemeral Network Ingress:** Utilizing free-tier ngrok tunnels generates randomized domain names that expire and cycle frequently, breaking Freshdesk webhook targets upon session reset.
- **Basic Fallback Boundaries:** Unanticipated model anomalies or database parsing formatting errors fall back straight to a hardcoded generic human escalation dictionary instead of evaluating progressive retry strategies.

---

## 🔮 Future Improvements

- **Cloud Infrastructure Integration:** Migrating local processes into production-ready containerized architectures (Docker, AWS ECS) paired with stable, dedicated API token gates.
- **Rigid Schema Validation:** Implementing Python `Pydantic` layers to rigorously check LLM text returns before execution to avoid JSON parsing failures.
- **Contextual Conversation Buffering:** Scaling vector query logic to support multi-turn message history, allowing the AI to understand continuous conversation streams rather than single ticket snapshots.

---

## 🎓 Key Learning Outcomes

- **Cognitive-Deterministic Hybridization:** Gained deep architectural insight into separating messy, human-centric cognitive reasoning (LLM processing) from immutable, policy-bound corporate requirements (Switch nodes and REST APIs).
- **Reverse Proxy Mesh Frameworks:** Mastered internal and external routing methods by bridging cloud SaaS environments with private local networks via secure websockets.
- **Asynchronous Data Engineering:** Architected high-performance, non-blocking Python backend systems capable of processing concurrent network data streams efficiently.
