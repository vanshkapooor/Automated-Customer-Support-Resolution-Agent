import requests
import json
import chromadb

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"

chroma_client = chromadb.PersistentClient(path="./chroma_db")
collection = chroma_client.get_collection(name="company_policies")

def analyze_ticket_with_llm(ticket_text: str) -> dict:
    """
    Processes raw ticket text using RAG to identify intent and draft responses based on company policy.
    """
    
    results = collection.query(
        query_texts=[ticket_text],
        n_results=3 
    )
    
    retrieved_context = "\n".join(results['documents'][0]) if results['documents'] else ""

    prompt = f"""
You are an automated customer support resolution agent with the ability to execute backend system tools.
You must strictly follow the Official Company Policies provided below.

--- OFFICIAL COMPANY POLICIES ---
{retrieved_context}
---------------------------------

Analyze the ticket and output ONLY a valid JSON object with the following keys:
1. "intent": Categorize the goal (e.g., 'password_reset', 'refund', 'fraud').
2. "action": Choose exactly one: 'auto_reply', 'escalate', or 'execute_tool'.
   - 'auto_reply': Choose this if the policy provides a clear answer or restriction, EVEN IF that rule means denying the customer's request (e.g., stating a digital product is non-refundable or past 30 days). A policy denial is a resolved issue and should NOT be escalated.
   - 'execute_tool': Choose this ONLY if the policy explicitly authorizes you to trigger a system action (like sending a password reset link).
   - 'escalate': Choose this ONLY for actual fraud reports, or when the policy explicitly states to escalate.
3. "tool_command": If action is 'execute_tool', output 'send_password_link'. Otherwise, output 'none'.
4. "draft_response": Write a polite message. If the request is denied based on policy, clearly explain the policy rule to the customer in a supportive tone.

Ticket Data:
"{ticket_text}"
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "format": "json",
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)
        response.raise_for_status()
        return json.loads(response.json()["response"])
        
    except Exception as e:
        print(f"Error communicating with LLM: {e}")
        return {
            "intent": "error", "action": "escalate", "tool_command": "none",
            "draft_response": "We have escalated your ticket to a human agent."
        }