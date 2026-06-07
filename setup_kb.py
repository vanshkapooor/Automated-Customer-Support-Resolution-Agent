import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(name="company_policies")

documents = [
    "Password Reset Policy: If a user forgets their password and requests a reset, you are authorized to use the backend system tool to email them a secure reset link. Do not escalate this.",
    "Refund Policy: Physical item refunds are only allowed within 30 days of purchase. The item must be in its original packaging. Digital software products are strictly non-refundable.",
    "Fraud Protocol: If a user reports an unauthorized or fraudulent charge, immediately escalate the ticket to the billing and security team. Do not attempt to process a refund manually. Inform the user their account is being locked down for their safety."
]

ids = ["policy_password", "policy_refund", "policy_fraud"]

collection.upsert(
    documents=documents,
    ids=ids
)

print("✅ Vector Knowledge Base built successfully!")