from fastapi import FastAPI, Request
from processor import analyze_ticket_with_llm
import uvicorn

app = FastAPI()

@app.post("/api/analyze-ticket")
async def analyze_ticket(request: Request):
    data = await request.json()
    ticket_text = data.get("ticket_text", "")
    
    if not ticket_text:
        return {"error": "No ticket text provided"}
    
    analysis_result = analyze_ticket_with_llm(ticket_text)
    
    return analysis_result

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)