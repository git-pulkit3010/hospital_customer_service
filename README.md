# Hospital Voice AI POC (v4.0)

A cost-effective Proof-of-Concept for a hospital voice assistant using **DeepSeek API** with local infrastructure for zero additional costs.

## 🏗️ Architecture Overview

| Component | POC Implementation | Production Path |
|-----------|-------------------|-----------------|
| **LLM Engine** | DeepSeek API | Same (or AWS Bedrock) |
| **Telephony** | Console I/O | AWS Connect / Twilio |
| **ASR/TTS** | Text Simulation | AWS Transcribe / Polly |
| **Vector DB** | Local Numpy + Sentence-Transformers | AWS OpenSearch / Pinecone |
| **Cache** | Local Dict + Cosine Similarity | AWS ElastiCache (Redis) |
| **Compliance** | Local JSONL Logs + PII Hashing | AWS CloudTrail + KMS |
| **Data Residency** | Local Storage (Simulates India) | AWS Mumbai/Hyderabad |

## 📁 Project Structure

```
Hospital_Chain_Service/
├── .env                    # Environment variables (DeepSeek API key)
├── .gitignore
├── requirements.txt        # Python dependencies
├── README.md
├── src/
│   ├── hospital_voice_poc.py    # Main POC script
│   └── load_mock_data.py        # Data verification script
├── data/
│   ├── mock_patient_db.json     # Mock patient records
│   ├── mock_knowledge_base.json # Hospital FAQ KB (20 categories)
│   ├── mock_audit_logs.jsonl    # Sample audit logs
│   └── mock_cache_store.json    # Sample cache entries
└── logs/
    └── audit_logs.jsonl         # Runtime audit logs (auto-generated)
```

## 🚀 Quick Start

### 1. Clone/Setup

Ensure you're in the project directory:
```bash
cd /home/pulkit3010/Documents/Hospital_Chain_Service
```

### 2. Create Virtual Environment (Optional but Recommended)

```bash
python -m venv venv
source venv/bin/activate  # On Linux/Mac
# or
venv\Scripts\activate     # On Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify Environment Variables

The `.env` file should contain your DeepSeek API key:
```bash
DEEPSEEK_API_KEY=sk-your-key-here
```

✅ Already configured in your `.env` file.

### 5. Verify Data Load

```bash
python src/load_mock_data.py
```

Expected output:
```
============================================================
🏥 HOSPITAL VOICE AI POC - DATA STATUS
============================================================
✅ Patient Database: data/mock_patient_db.json
✅ Knowledge Base: data/mock_knowledge_base.json
✅ Audit Logs: data/mock_audit_logs.jsonl
✅ Cache Store: data/mock_cache_store.json

📊 MOCK DATA STATISTICS:
   - Patient Records: 5
   - FAQ Categories: 20
   - Cache Entries: 5
   - Cache Hit Rate: 73%
   - Est. Cost Savings: ₹2,340 per month

🛡️  COMPLIANCE STATUS:
   - Data Region: India (Simulated)
   - DPDPA Compliant: ✅ (All data fictional)
   - Audit Logging: ✅ (WORM simulation)
============================================================
```

### 6. Run the POC

```bash
python src/hospital_voice_poc.py
```

## 🎮 Test Scenarios

| Scenario | Phone Number | Query | Expected Result |
|----------|--------------|-------|-----------------|
| **Billing Inquiry** | 9876543210 | "What is my bill amount?" | ₹1,200 Pending |
| **Report Status** | 9876543210 | "Is my report ready?" | Ready for Pickup |
| **Appointment Check** | 9123456789 | "When is my appointment?" | Pending Reschedule |
| **FAQ - Visiting Hours** | Any | "When can I visit?" | 10 AM-12 PM, 4 PM-7 PM |
| **FAQ - Emergency** | Any | "Is emergency 24/7?" | Yes, Gate 1 |
| **Medical Guardrail** | Any | "I have chest pain" | BLOCKED → Escalate |
| **Human Handoff** | Any | "I want to speak to agent" | ESCALATED with context |
| **Cache Hit Demo** | Any | "What are the visiting hours?" (2nd time) | ⚡ CACHED (<100ms) |

## 🛡️ Compliance Features (DPDPA 2023)

- **Data Residency**: All data stored locally (simulates India region)
- **PII Protection**: Phone numbers hashed using SHA-256 before logging
- **Audit Trails**: Immutable JSONL logs with timestamps
- **Consent Management**: Simulated consent script at call start
- **Medical Guardrails**: Hard-coded filters for medical terms

## 🔧 Configuration

Edit `.env` file to customize:

```bash
DEEPSEEK_API_KEY=sk-your-key-here
```

Edit `src/hospital_voice_poc.py` to customize:

```python
CONFIG = {
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
    "DATA_REGION": "India (Local Storage)",
    "MEDICAL_GUARDRAILS": ["symptom", "diagnosis", "treatment", "dosage", "medicine", "prescription"]
}
```

## 📊 Mock Data

### Patient Database (`data/mock_patient_db.json`)
- 5 fictional patient records
- Indian names, phone formats, ₹ currency
- Includes: appointments, billing, insurance, reports

### Knowledge Base (`data/mock_knowledge_base.json`)
- 20 FAQ categories covering:
  - Visiting hours, Billing, Emergency
  - Appointments, Insurance, Reports
  - Parking, Pharmacy, Dietary
  - And more...

### Audit Logs (`logs/audit_logs.jsonl`)
- Auto-generated during runtime
- Contains: timestamp, session_id, phone_hash, input, output, action, region, latency

## 🏥 Production Migration Path

When ready for production:

1. **Replace `VoiceInterface`** → AWS Connect Media Streams
2. **Replace `LocalRAGStore`** → AWS OpenSearch Serverless
3. **Replace `SemanticCache`** → AWS ElastiCache (Redis)
4. **Replace `ComplianceLogger`** → AWS CloudWatch + S3 (WORM)
5. **Deploy to** → AWS Mumbai Region (`ap-south-1`)

## 💰 Cost Breakdown

| Component | POC Cost | Production Cost |
|-----------|----------|-----------------|
| DeepSeek API | ~$0.002/request | ~$0.002/request |
| Compute | $0 (Local) | ~$50-100/month (EC2/Lambda) |
| Vector DB | $0 (Local) | ~$100-300/month (OpenSearch) |
| Cache | $0 (Local) | ~$50-150/month (ElastiCache) |
| Telephony | $0 (Simulated) | ~$0.015/min (Connect) |
| **Total** | **~$0.002/request** | **~$200-600/month + usage** |

## 📝 License

This POC is for demonstration purposes. All mock data is fictional.

## 🤝 Support

For issues or questions, check the documentation files:
- `Codebase - Overview V4.md` - Architecture overview
- `Dataset and Ingestion.md` - Data specifications
