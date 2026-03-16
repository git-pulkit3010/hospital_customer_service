Yes. Below are **comprehensive mock datasets** designed specifically for your POC. These are realistic enough to demonstrate all key features (RAG, Caching, Compliance, Handoff) while being completely fictional and safe to use.

I've organized them into **4 files** that you can drop directly into your POC folder.

---

## **1. Mock Patient Database** (`mock_patient_db.json`)
*Simulates Hospital Information System (HIS) records*

```json
{
  "metadata": {
    "description": "Mock Patient Records for POC",
    "compliance": "DPDPA 2023 - All data is fictional, no real PHI",
    "region": "India (Simulated)",
    "last_updated": "2025-01-15"
  },
  "patients": {
    "9876543210": {
      "patient_id": "PT-2024-001",
      "name": "Arjun Sharma",
      "age": 34,
      "gender": "Male",
      "phone": "9876543210",
      "email": "arjun.s@example.com",
      "registration_date": "2024-06-15",
      "last_visit": "2025-01-10",
      "department": "Cardiology",
      "doctor": "Dr. Priya Mehta",
      "appointment_status": "Confirmed",
      "next_appointment": "2025-01-20 10:00 AM",
      "bill_status": "Pending",
      "bill_amount": "₹1,200",
      "insurance_provider": "Star Health",
      "insurance_policy": "SH-987654321",
      "report_status": "Ready for Pickup",
      "admission_status": "Outpatient"
    },
    "9123456789": {
      "patient_id": "PT-2024-002",
      "name": "Priya Patel",
      "age": 28,
      "gender": "Female",
      "phone": "9123456789",
      "email": "priya.p@example.com",
      "registration_date": "2024-08-20",
      "last_visit": "2025-01-12",
      "department": "Orthopedics",
      "doctor": "Dr. Rajesh Kumar",
      "appointment_status": "Pending Reschedule",
      "next_appointment": "To Be Scheduled",
      "bill_status": "Paid",
      "bill_amount": "₹0",
      "insurance_provider": "HDFC Ergo",
      "insurance_policy": "HDFC-123456789",
      "report_status": "Pending",
      "admission_status": "Outpatient"
    },
    "9988776655": {
      "patient_id": "PT-2024-003",
      "name": "Vikram Singh",
      "age": 45,
      "gender": "Male",
      "phone": "9988776655",
      "email": "vikram.s@example.com",
      "registration_date": "2024-03-10",
      "last_visit": "2025-01-08",
      "department": "General Medicine",
      "doctor": "Dr. Anjali Desai",
      "appointment_status": "Completed",
      "next_appointment": "2025-02-01 03:00 PM",
      "bill_status": "Paid",
      "bill_amount": "₹850",
      "insurance_provider": "ICICI Lombard",
      "insurance_policy": "ICICI-555666777",
      "report_status": "Sent via Email",
      "admission_status": "Outpatient"
    },
    "9112233445": {
      "patient_id": "PT-2024-004",
      "name": "Sneha Reddy",
      "age": 52,
      "gender": "Female",
      "phone": "9112233445",
      "email": "sneha.r@example.com",
      "registration_date": "2024-11-05",
      "last_visit": "2025-01-14",
      "department": "Neurology",
      "doctor": "Dr. Amit Verma",
      "appointment_status": "Cancelled",
      "next_appointment": "To Be Scheduled",
      "bill_status": "Refund Processing",
      "bill_amount": "₹0",
      "insurance_provider": "Bajaj Allianz",
      "insurance_policy": "BAJAJ-999888777",
      "report_status": "Not Applicable",
      "admission_status": "Outpatient"
    },
    "9554433221": {
      "patient_id": "PT-2024-005",
      "name": "Rahul Gupta",
      "age": 39,
      "gender": "Male",
      "phone": "9554433221",
      "email": "rahul.g@example.com",
      "registration_date": "2024-07-22",
      "last_visit": "2025-01-13",
      "department": "Pediatrics",
      "doctor": "Dr. Sunita Rao",
      "appointment_status": "Confirmed",
      "next_appointment": "2025-01-18 11:30 AM",
      "bill_status": "Pending",
      "bill_amount": "₹2,500",
      "insurance_provider": "Max Bupa",
      "insurance_policy": "MAX-111222333",
      "report_status": "Pending",
      "admission_status": "Outpatient"
    }
  }
}
```

---

## **2. Hospital FAQ Knowledge Base** (`mock_knowledge_base.json`)
*For RAG retrieval (Top 20 FAQs as per Overview V4.md)*

```json
{
  "metadata": {
    "description": "Hospital FAQ Knowledge Base for RAG",
    "version": "1.0",
    "last_updated": "2025-01-15",
    "compliance": "All information verified by Hospital Administration",
    "region": "India"
  },
  "categories": {
    "visiting_hours": {
      "category_id": "FAQ-001",
      "questions": [
        "What are the visiting hours?",
        "When can I meet the patient?",
        "Visiting time schedule"
      ],
      "answer": "Visiting hours are 10:00 AM to 12:00 PM and 4:00 PM to 7:00 PM daily. Only 2 visitors are allowed per patient at a time. Please carry a valid ID proof.",
      "tags": ["visiting", "hours", "timing", "meeting"]
    },
    "billing_counter": {
      "category_id": "FAQ-002",
      "questions": [
        "Where is the billing counter?",
        "Billing section location",
        "Where do I pay the bill?"
      ],
      "answer": "The billing counter is located on the Ground Floor, near the main entrance. It is open 24/7 for emergency billing. Regular hours: 8:00 AM to 8:00 PM.",
      "tags": ["billing", "payment", "counter", "location"]
    },
    "emergency_services": {
      "category_id": "FAQ-003",
      "questions": [
        "Is emergency available 24/7?",
        "Emergency services timing",
        "Casualty department hours"
      ],
      "answer": "Yes, Emergency Services are available 24/7 at Gate 1. Ambulance services can be reached at 108 or our hospital number 040-1234-5678.",
      "tags": ["emergency", "24/7", "casualty", "ambulance"]
    },
    "appointment_reschedule": {
      "category_id": "FAQ-004",
      "questions": [
        "How do I reschedule my appointment?",
        "Change appointment date",
        "Cancel and rebook appointment"
      ],
      "answer": "To reschedule an appointment, please call 1800-123-4567 or visit the reception desk. Rescheduling must be done at least 24 hours before the scheduled time to avoid charges.",
      "tags": ["appointment", "reschedule", "cancel", "rebook"]
    },
    "insurance_claims": {
      "category_id": "FAQ-005",
      "questions": [
        "What documents are needed for insurance?",
        "Insurance claim process",
        "Cashless treatment documents"
      ],
      "answer": "For insurance claims, please carry: (1) Valid ID Proof, (2) Insurance Policy Card, (3) Doctor's Prescription, (4) Previous Medical Records. Cashless approval takes 2-4 hours.",
      "tags": ["insurance", "claims", "documents", "cashless"]
    },
    "report_collection": {
      "category_id": "FAQ-006",
      "questions": [
        "How do I collect my lab report?",
        "Report pickup timing",
        "When will my test results be ready?"
      ],
      "answer": "Lab reports are available within 24-48 hours. You can collect them from the Reception Desk (Ground Floor) or download from our patient portal. Bring your UHID card for collection.",
      "tags": ["report", "lab", "test", "results", "collection"]
    },
    "parking_facility": {
      "category_id": "FAQ-007",
      "questions": [
        "Is parking available?",
        "Parking charges",
        "Where can I park my vehicle?"
      ],
      "answer": "Yes, we have a multi-level parking facility. Charges: ₹50 for 2-wheeler, ₹100 for 4-wheeler (first 4 hours). Free parking for emergency cases.",
      "tags": ["parking", "vehicle", "charges", "facility"]
    },
    "pharmacy_hours": {
      "category_id": "FAQ-008",
      "questions": [
        "Is the pharmacy open 24/7?",
        "Where is the hospital pharmacy?",
        "Medicine shop timing"
      ],
      "answer": "The hospital pharmacy is located on the Ground Floor and is open 24/7. We also have an external pharmacy near Gate 2 open from 8:00 AM to 10:00 PM.",
      "tags": ["pharmacy", "medicine", "timing", "hours"]
    },
    "dietary_services": {
      "category_id": "FAQ-009",
      "questions": [
        "Can I bring outside food?",
        "Hospital food service",
        "Diet for patients"
      ],
      "answer": "Outside food is allowed but should be homemade and hygienic. The hospital provides dietary meals for admitted patients as per doctor's prescription. Cafeteria is open 7:00 AM to 9:00 PM.",
      "tags": ["food", "diet", "outside", "cafeteria"]
    },
    "visitor_pass": {
      "category_id": "FAQ-010",
      "questions": [
        "Do I need a visitor pass?",
        "How to get entry pass?",
        "Visitor registration"
      ],
      "answer": "Yes, all visitors must register at the security desk and obtain a visitor pass. Please carry a valid government ID (Aadhaar, Driving License, etc.).",
      "tags": ["visitor", "pass", "entry", "registration", "ID"]
    },
    "wheelchair_service": {
      "category_id": "FAQ-011",
      "questions": [
        "Is wheelchair available?",
        "Wheelchair rental",
        "Mobility assistance"
      ],
      "answer": "Wheelchairs are available free of charge at the main entrance. Please deposit a refundable amount of ₹500 or leave your ID card. Return within 2 hours.",
      "tags": ["wheelchair", "mobility", "assistance", "rental"]
    },
    "discharge_process": {
      "category_id": "FAQ-012",
      "questions": [
        "What is the discharge procedure?",
        "How long does discharge take?",
        "Discharge summary"
      ],
      "answer": "Discharge process takes 2-3 hours after doctor's approval. You need to clear all bills at the billing counter and collect discharge summary, prescriptions, and reports from the nursing station.",
      "tags": ["discharge", "procedure", "summary", "billing"]
    },
    "second_opinion": {
      "category_id": "FAQ-013",
      "questions": [
        "Can I get a second opinion?",
        "Second opinion appointment",
        "Consult another doctor"
      ],
      "answer": "Yes, second opinion consultations are available. Please book an appointment through our helpline 1800-123-4567. Bring all previous medical records and reports.",
      "tags": ["second opinion", "consultation", "doctor"]
    },
    "health_checkup": {
      "category_id": "FAQ-014",
      "questions": [
        "Do you offer health checkup packages?",
        "Full body checkup cost",
        "Preventive health screening"
      ],
      "answer": "Yes, we offer comprehensive health checkup packages starting from ₹1,500. Packages include basic, standard, and premium options. Call 1800-123-4567 for booking.",
      "tags": ["checkup", "package", "screening", "preventive"]
    },
    "vaccination_services": {
      "category_id": "FAQ-015",
      "questions": [
        "Do you provide vaccination?",
        "Vaccine availability",
        "Immunization services"
      ],
      "answer": "Yes, vaccination services are available for children and adults. Timings: Monday to Saturday, 9:00 AM to 5:00 PM. No appointment needed for routine vaccines.",
      "tags": ["vaccination", "vaccine", "immunization", "injection"]
    },
    "ambulance_service": {
      "category_id": "FAQ-016",
      "questions": [
        "How to book an ambulance?",
        "Ambulance charges",
        "Emergency transport"
      ],
      "answer": "Ambulance can be booked by calling 108 (government) or 040-1234-5678 (hospital). Charges: ₹500 within city limits, ₹10/km beyond. ICU ambulance available for critical patients.",
      "tags": ["ambulance", "transport", "emergency", "booking"]
    },
    "online_consultation": {
      "category_id": "FAQ-017",
      "questions": [
        "Do you have online consultation?",
        "Telemedicine service",
        "Video call with doctor"
      ],
      "answer": "Yes, online consultation is available through our patient portal and mobile app. Charges: ₹300 for general consultation, ₹500 for specialist. Available 9:00 AM to 6:00 PM.",
      "tags": ["online", "telemedicine", "video", "consultation"]
    },
    "medical_records": {
      "category_id": "FAQ-018",
      "questions": [
        "How to get old medical records?",
        "Request past reports",
        "Medical history copy"
      ],
      "answer": "To request old medical records, submit a written application at the Medical Records Department (1st Floor). Processing time: 3-5 working days. Fee: ₹100 per page.",
      "tags": ["records", "history", "reports", "documents"]
    },
    "complaint_feedback": {
      "category_id": "FAQ-019",
      "questions": [
        "Where do I file a complaint?",
        "Feedback mechanism",
        "Patient grievance"
      ],
      "answer": "Complaints can be filed at the Patient Relations Desk (Ground Floor) or via email at feedback@hospital.com. We respond within 48 hours. Helpline: 1800-123-4567.",
      "tags": ["complaint", "feedback", "grievance", "relations"]
    },
    "covid_protocol": {
      "category_id": "FAQ-020",
      "questions": [
        "What are the COVID safety measures?",
        "Mask mandatory?",
        "COVID testing available?"
      ],
      "answer": "Masks are recommended in clinical areas. RT-PCR testing is available from 8:00 AM to 6:00 PM (Report in 24 hours). Rapid Antigen Test available 24/7 (Report in 1 hour).",
      "tags": ["covid", "mask", "testing", "safety", "protocol"]
    }
  }
}
```

---

## **3. Mock Audit Logs** (`mock_audit_logs.jsonl`)
*Demonstrates DPDPA 2023 compliance logging (WORM simulation)*

```json
{"timestamp": "2025-01-15T09:15:23", "session_id": "sess-001-abc123", "phone_hash": "a1b2c3d4e5f6...", "input": "What are the visiting hours?", "output": "Visiting hours are 10:00 AM to 12:00 PM and 4:00 PM to 7:00 PM daily.", "action": "CACHED", "region": "India-Mumbai", "latency_ms": 120}
{"timestamp": "2025-01-15T09:16:45", "session_id": "sess-002-def456", "phone_hash": "b2c3d4e5f6g7...", "input": "Is my report ready?", "output": "Your report is Ready for Pickup. Please collect from Reception Desk with your UHID card.", "action": "ANSWERED", "region": "India-Mumbai", "latency_ms": 850}
{"timestamp": "2025-01-15T09:18:12", "session_id": "sess-003-ghi789", "phone_hash": "c3d4e5f6g7h8...", "input": "I have chest pain, what should I do?", "output": "I cannot provide medical advice. Please hang up and dial emergency services or visit the nearest emergency department.", "action": "BLOCKED_MEDICAL", "region": "India-Mumbai", "latency_ms": 50}
{"timestamp": "2025-01-15T09:20:33", "session_id": "sess-004-jkl012", "phone_hash": "d4e5f6g7h8i9...", "input": "I want to speak to a human agent", "output": "Please hold while I connect you to a human agent.", "action": "ESCALATED", "region": "India-Mumbai", "latency_ms": 200}
{"timestamp": "2025-01-15T09:22:01", "session_id": "sess-005-mno345", "phone_hash": "e5f6g7h8i9j0...", "input": "Where is the billing counter?", "output": "The billing counter is located on the Ground Floor, near the main entrance.", "action": "CACHED", "region": "India-Mumbai", "latency_ms": 95}
```

---

## **4. Mock Cache Store** (`mock_cache_store.json`)
*Demonstrates Semantic Caching functionality*

```json
{
  "metadata": {
    "description": "Semantic Cache Store for POC",
    "cache_version": "1.0",
    "hit_rate_target": ">95% for top 20 FAQs",
    "invalidation_policy": "24-hour refresh for high-volume entries"
  },
  "cache_entries": [
    {
      "query_embedding_hash": "emb_hash_001",
      "original_query": "What are the visiting hours?",
      "cached_response": "Visiting hours are 10:00 AM to 12:00 PM and 4:00 PM to 7:00 PM daily. Only 2 visitors are allowed per patient at a time.",
      "hit_count": 145,
      "last_accessed": "2025-01-15T09:15:23",
      "created_at": "2025-01-10T08:00:00",
      "kb_version": "1.0"
    },
    {
      "query_embedding_hash": "emb_hash_002",
      "original_query": "Where is the billing counter?",
      "cached_response": "The billing counter is located on the Ground Floor, near the main entrance. It is open 24/7 for emergency billing.",
      "hit_count": 98,
      "last_accessed": "2025-01-15T09:22:01",
      "created_at": "2025-01-10T08:00:00",
      "kb_version": "1.0"
    },
    {
      "query_embedding_hash": "emb_hash_003",
      "original_query": "How do I reschedule my appointment?",
      "cached_response": "To reschedule an appointment, please call 1800-123-4567 or visit the reception desk. Rescheduling must be done at least 24 hours before the scheduled time.",
      "hit_count": 67,
      "last_accessed": "2025-01-15T08:45:12",
      "created_at": "2025-01-10T08:00:00",
      "kb_version": "1.0"
    },
    {
      "query_embedding_hash": "emb_hash_004",
      "original_query": "Is emergency available 24/7?",
      "cached_response": "Yes, Emergency Services are available 24/7 at Gate 1. Ambulance services can be reached at 108 or our hospital number 040-1234-5678.",
      "hit_count": 203,
      "last_accessed": "2025-01-15T09:30:45",
      "created_at": "2025-01-10T08:00:00",
      "kb_version": "1.0"
    },
    {
      "query_embedding_hash": "emb_hash_005",
      "original_query": "What documents are needed for insurance?",
      "cached_response": "For insurance claims, please carry: (1) Valid ID Proof, (2) Insurance Policy Card, (3) Doctor's Prescription, (4) Previous Medical Records.",
      "hit_count": 54,
      "last_accessed": "2025-01-15T07:20:33",
      "created_at": "2025-01-10T08:00:00",
      "kb_version": "1.0"
    }
  ],
  "statistics": {
    "total_entries": 5,
    "total_hits": 567,
    "cache_hit_rate": "73%",
    "avg_latency_saved_ms": 750,
    "estimated_cost_savings": "₹2,340 per month"
  }
}
```

---

## **5. Integration Script** (`load_mock_data.py`)
*Helper script to load all mock data into the POC*

```python
import json
import os

def load_patient_db():
    """Load mock patient database"""
    with open('mock_patient_db.json', 'r') as f:
        return json.load(f)

def load_knowledge_base():
    """Load mock FAQ knowledge base"""
    with open('mock_knowledge_base.json', 'r') as f:
        return json.load(f)

def load_audit_logs():
    """Load mock audit logs"""
    logs = []
    with open('mock_audit_logs.jsonl', 'r') as f:
        for line in f:
            logs.append(json.loads(line))
    return logs

def load_cache_store():
    """Load mock cache store"""
    with open('mock_cache_store.json', 'r') as f:
        return json.load(f)

def print_poc_dashboard():
    """Display POC status dashboard"""
    print("\n" + "="*60)
    print("🏥 HOSPITAL VOICE AI POC - DATA STATUS")
    print("="*60)
    
    # Check files
    files = {
        "Patient Database": "mock_patient_db.json",
        "Knowledge Base": "mock_knowledge_base.json",
        "Audit Logs": "mock_audit_logs.jsonl",
        "Cache Store": "mock_cache_store.json"
    }
    
    for name, file in files.items():
        status = "✅" if os.path.exists(file) else "❌"
        print(f"{status} {name}: {file}")
    
    # Load and display stats
    patient_db = load_patient_db()
    kb = load_knowledge_base()
    cache = load_cache_store()
    
    print("\n📊 MOCK DATA STATISTICS:")
    print(f"   - Patient Records: {len(patient_db['patients'])}")
    print(f"   - FAQ Categories: {len(kb['categories'])}")
    print(f"   - Cache Entries: {cache['statistics']['total_entries']}")
    print(f"   - Cache Hit Rate: {cache['statistics']['cache_hit_rate']}")
    print(f"   - Est. Cost Savings: {cache['statistics']['estimated_cost_savings']}")
    
    print("\n🛡️  COMPLIANCE STATUS:")
    print(f"   - Data Region: {patient_db['metadata']['region']}")
    print(f"   - DPDPA Compliant: ✅ (All data fictional)")
    print(f"   - Audit Logging: ✅ (WORM simulation)")
    
    print("="*60 + "\n")

if __name__ == "__main__":
    print_poc_dashboard()
```

---

## **How to Use These Datasets**

### **Step 1: Save All Files**
```bash
mkdir hospital_poc_data
cd hospital_poc_data
# Save each code block above as separate files
```

### **Step 2: Verify Data Load**
```bash
python load_mock_data.py
```

**Expected Output:**
```
============================================================
🏥 HOSPITAL VOICE AI POC - DATA STATUS
============================================================
✅ Patient Database: mock_patient_db.json
✅ Knowledge Base: mock_knowledge_base.json
✅ Audit Logs: mock_audit_logs.jsonl
✅ Cache Store: mock_cache_store.json

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

### **Step 3: Run POC with Mock Data**
```bash
python hospital_voice_poc.py
```

---

## **Test Scenarios You Can Demonstrate**

| Scenario | Phone Number | Query | Expected Result |
| :--- | :--- | :--- | :--- |
| **Billing Inquiry** | 9876543210 | "What is my bill amount?" | ₹1,200 Pending |
| **Report Status** | 9876543210 | "Is my report ready?" | Ready for Pickup |
| **Appointment Check** | 9123456789 | "When is my appointment?" | Pending Reschedule |
| **FAQ - Visiting Hours** | Any | "When can I visit?" | 10 AM-12 PM, 4 PM-7 PM |
| **FAQ - Emergency** | Any | "Is emergency 24/7?" | Yes, Gate 1 |
| **Medical Guardrail** | Any | "I have chest pain" | BLOCKED → Escalate |
| **Human Handoff** | Any | "I want to speak to agent" | ESCALATED with context |
| **Cache Hit Demo** | Any | "What are the visiting hours?" (2nd time) | ⚡ CACHED (<100ms) |

---

## **Why This Data Works for POC**

| Requirement | How This Data Meets It |
| :--- | :--- |
| **Realistic** | Indian names, phone formats, ₹ currency, local hospital structure |
| **Compliant** | All fictional data, no real PHI, DPDPA 2023 aligned |
| **Comprehensive** | Covers all 20 top FAQs from Overview V4.md |
| **Demonstrable** | Clear cache hits, escalations, and guardrail triggers |
| **Scalable** | JSON format easy to expand for production |
| **Auditable** | Complete audit trail with timestamps and actions |

---

## **Next Steps**

1. **Save all 5 files** in your POC directory
2. **Run `load_mock_data.py`** to verify everything loads
3. **Run `hospital_voice_poc.py`** and test the scenarios above
4. **Record a demo video** showing cache hits, escalations, and guardrails
5. **Present to stakeholders** with the dashboard output

This mock dataset is **production-ready in structure** but **safe for POC use**. When you move to production, you simply swap these JSON files for real database connections without changing the AI logic.