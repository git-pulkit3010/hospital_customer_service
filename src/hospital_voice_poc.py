"""
Hospital Voice AI POC (v4.0)
Cost: $0.00 (except DeepSeek API tokens)
Compliance: Simulated DPDPA 2023 (Local Logging, Consent Checks, Guardrails)
"""

import os
import json
import time
import uuid
import hashlib
import numpy as np
from datetime import datetime
from abc import ABC, abstractmethod
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Try to import sentence-transformers for semantic caching (Free & Local)
try:
    from sentence_transformers import SentenceTransformer
    EMBEDDING_MODEL = SentenceTransformer('all-MiniLM-L6-v2')
    HAS_EMBEDDINGS = True
except ImportError:
    HAS_EMBEDDINGS = False
    print("⚠️  Warning: sentence-transformers not found. Using basic hashing for cache.")

# OpenAI client for DeepSeek API
try:
    from openai import OpenAI
except ImportError:
    print("❌ Error: openai package not installed. Run: pip install openai")
    exit(1)

# Get the base directory (where the script is located)
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"
LOGS_DIR = BASE_DIR / "logs"

# Ensure logs directory exists
LOGS_DIR.mkdir(exist_ok=True)

# ---------------------------------------------------------
# 0. Configuration & Compliance Constants (DPDPA 2023)
# ---------------------------------------------------------
CONFIG = {
    "DEEPSEEK_API_KEY": os.getenv("DEEPSEEK_API_KEY", ""),
    "DEEPSEEK_BASE_URL": "https://api.deepseek.com",
    "DATA_REGION": "India (Local Storage)",  # Simulating Mumbai/Hyderabad residency
    "CONSENT_SCRIPT": "Hello, this is your AI assistant from City Hospital. This call may be recorded for quality purposes. If you do not consent, please say 'opt out'.",
    "MEDICAL_GUARDRAILS": ["symptom", "diagnosis", "treatment", "dosage", "medicine", "prescription"]
}

# ---------------------------------------------------------
# 1. Audit & Compliance Logger (WORM Simulation)
# ---------------------------------------------------------
class ComplianceLogger:
    def __init__(self):
        self.log_file = LOGS_DIR / "audit_logs.jsonl"
        # Ensure file exists
        if not self.log_file.exists():
            with open(self.log_file, 'w') as f: 
                pass

    def log_interaction(self, session_id, phone, input_text, output_text, action, latency_ms=0):
        """Logs interaction for DPDPA 2023 audit trails (Immutable Append)"""
        entry = {
            "timestamp": datetime.now().isoformat(),
            "session_id": session_id,
            "phone_hash": hashlib.sha256(phone.encode() if phone else b"unknown").hexdigest(),
            "input": input_text,
            "output": output_text,
            "action": action,
            "region": CONFIG["DATA_REGION"],
            "latency_ms": latency_ms
        }
        with open(self.log_file, 'a') as f:
            f.write(json.dumps(entry) + "\n")

# ---------------------------------------------------------
# 2. Semantic Cache (Local Redis Alternative)
# ---------------------------------------------------------
class SemanticCache:
    def __init__(self):
        self.cache = {}  # { embedding_vector_bytes : response }
        self.threshold = 0.85  # Similarity threshold

    def _get_embedding(self, text):
        if HAS_EMBEDDINGS:
            return EMBEDDING_MODEL.encode(text)
        else:
            # Fallback: simple hash (not truly semantic, but functional for POC)
            return np.array([ord(c) for c in text[:50]], dtype=np.float64)

    def get(self, query):
        query_vec = self._get_embedding(query)
        for stored_vec_bytes, response in self.cache.items():
            stored_vec = np.frombuffer(stored_vec_bytes, dtype=query_vec.dtype)
            # Check dimension match first
            if query_vec.shape != stored_vec.shape:
                continue
            # Calculate Cosine Similarity
            similarity = np.dot(query_vec, stored_vec) / (
                np.linalg.norm(query_vec) * np.linalg.norm(stored_vec)
            )
            if similarity > self.threshold:
                return response
        return None

    def set(self, query, response):
        vec = self._get_embedding(query)
        self.cache[vec.tobytes()] = response

# ---------------------------------------------------------
# 3. The Data Interface (Refactoring Shield)
# ---------------------------------------------------------
class HospitalDataConnector(ABC):
    @abstractmethod
    def get_patient_record(self, phone_number):
        pass

class MockHISConnector(HospitalDataConnector):
    def __init__(self):
        self.data = {}
        self._load_mock_data()

    def _load_mock_data(self):
        """Load mock patient data from JSON file"""
        patient_db_path = DATA_DIR / "mock_patient_db.json"
        if patient_db_path.exists():
            with open(patient_db_path, 'r') as f:
                data = json.load(f)
                self.data = data.get('patients', {})
        else:
            # Fallback inline data
            self.data = {
                "9876543210": {"name": "Arjun Sharma", "status": "Report Ready", "bill": "₹1200"},
                "9123456789": {"name": "Priya Patel", "status": "Appointment Pending", "bill": "₹0"}
            }

    def get_patient_record(self, phone_number):
        return self.data.get(phone_number, "No record found.")

# ---------------------------------------------------------
# 4. RAG Knowledge Base (Local Vector Store)
# ---------------------------------------------------------
class LocalRAGStore:
    def __init__(self):
        self.documents = []
        self.answers = {}
        self.embeddings = []
        self._load_knowledge_base()

    def _load_knowledge_base(self):
        """Load FAQ knowledge base from JSON file"""
        kb_path = DATA_DIR / "mock_knowledge_base.json"
        if kb_path.exists():
            with open(kb_path, 'r') as f:
                data = json.load(f)
                categories = data.get('categories', {})
                for key, category in categories.items():
                    doc = f"{category['answer']}"
                    self.documents.append(doc)
                    for question in category['questions']:
                        self.answers[question.lower()] = doc
        else:
            # Fallback inline data
            self.documents = [
                "Visiting hours are 10 AM to 12 PM and 4 PM to 7 PM.",
                "Billing counter is open 24/7 on the Ground Floor.",
                "Emergency services are available 24/7 at Gate 1.",
                "To reschedule an appointment, call 1800-123-4567.",
                "Insurance claims require ID proof and policy number."
            ]

        # Generate embeddings
        if HAS_EMBEDDINGS and self.documents:
            self.embeddings = EMBEDDING_MODEL.encode(self.documents)

    def search(self, query, top_k=1):
        # Check exact question match first
        query_lower = query.lower()
        for question, answer in self.answers.items():
            if question in query_lower or query_lower in question:
                return answer

        if not HAS_EMBEDDINGS or len(self.embeddings) == 0:
            # Fallback: Keyword match
            for doc in self.documents:
                if any(word in doc.lower() for word in query_lower.split()):
                    return doc
            return self.documents[0] if self.documents else "No information available."

        query_vec = EMBEDDING_MODEL.encode(query)
        similarities = np.dot(self.embeddings, query_vec) / (
            np.linalg.norm(self.embeddings, axis=1) * np.linalg.norm(query_vec)
        )
        top_idx = np.argsort(similarities)[::-1][:top_k]
        return self.documents[top_idx[0]]

# ---------------------------------------------------------
# 5. Voice Interface (Simulated Telephony)
# ---------------------------------------------------------
class VoiceInterface:
    """
    Simulates AWS Connect + ASR + TTS.
    In Production, this would stream audio via WebSockets.
    """
    def listen(self):
        # Simulates ASR (Speech-to-Text)
        return input("\n🎤 Patient (You): ")

    def speak(self, text):
        # Simulates TTS (Text-to-Speech)
        print(f"🤖 AI Agent: {text}")

# ---------------------------------------------------------
# 6. The AI Core (Logic & Guardrails)
# ---------------------------------------------------------
class HospitalAI:
    def __init__(self, data_connector: HospitalDataConnector):
        self.db = data_connector
        self.client = OpenAI(
            api_key=CONFIG["DEEPSEEK_API_KEY"],
            base_url=CONFIG["DEEPSEEK_BASE_URL"]
        )
        self.cache = SemanticCache()
        self.rag = LocalRAGStore()
        self.logger = ComplianceLogger()
        self.session_id = str(uuid.uuid4())

    def _check_medical_guardrails(self, query):
        """Hard-coded safety per Overview V4.md Section 5.4"""
        query_lower = query.lower()
        for term in CONFIG["MEDICAL_GUARDRAILS"]:
            if term in query_lower:
                return True
        return False

    def _escalate_to_human(self, context, reason):
        """Handles Handoff per Overview V4.md Section 3.2"""
        print("\n⚠️  ESCALATION TRIGGERED")
        print(f"📞 Transferring to Human Agent...")
        print(f"📄 Context Transferred: {context}")
        print(f"📄 Reason: {reason}")
        self.logger.log_interaction(
            self.session_id, "unknown", context, "ESCALATED", reason
        )
        return "Please hold while I connect you to a specialist."

    def handle_query(self, user_query, phone=None):
        start_time = time.time()

        # 1. Compliance: Consent Check (Simulated)
        if user_query.lower().startswith("opt out"):
            return "Call terminated per user consent opt-out."

        # 2. Safety: Medical Guardrails
        if self._check_medical_guardrails(user_query):
            response = "I cannot provide medical advice. Please consult your treating physician or visit the Emergency Department."
            self.logger.log_interaction(
                self.session_id, phone, user_query, response, "BLOCKED_MEDICAL"
            )
            return response

        # 3. Performance: Semantic Cache Check
        cached_response = self.cache.get(user_query)
        if cached_response:
            print("⚡ [Cache Hit]")
            self.logger.log_interaction(
                self.session_id, phone, user_query, cached_response, "CACHED"
            )
            return cached_response

        # 4. RAG: Retrieve Context
        rag_context = self.rag.search(user_query)
        patient_context = "No patient context."
        if phone:
            patient_context = self.db.get_patient_record(phone)

        # 5. Generation: DeepSeek API
        prompt = f"""
        You are a helpful hospital assistant.
        Patient Info: {patient_context}
        Hospital Policy Context: {rag_context}
        User Query: {user_query}

        Instructions:
        - Be concise.
        - If unsure, escalate.
        - Do not give medical advice.
        """

        try:
            completion = self.client.chat.completions.create(
                model="deepseek-chat",
                messages=[{"role": "user", "content": prompt}],
                stream=False
            )
            response = completion.choices[0].message.content
        except Exception as e:
            response = "I'm having trouble connecting. Let me transfer you to a human."
            return self._escalate_to_human(user_query, str(e))

        # Calculate latency
        latency_ms = int((time.time() - start_time) * 1000)

        # 6. Cache Save
        self.cache.set(user_query, response)
        self.logger.log_interaction(
            self.session_id, phone, user_query, response, "ANSWERED", latency_ms
        )
        return response

# ---------------------------------------------------------
# 7. Execution Loop (POC Simulation)
# ---------------------------------------------------------
def run_poc():
    print("🏥 Hospital Voice AI POC (v4.0)")
    print(f"🌍 Data Region: {CONFIG['DATA_REGION']}")
    print("🛡️  Compliance: DPDPA 2023 Simulated")
    print("-" * 40)

    # Initialize System
    bot = HospitalAI(data_connector=MockHISConnector())
    voice = VoiceInterface()

    # Simulate Call Start
    print(f"\n🔔 Incoming Call...")
    print(f"🤖 {CONFIG['CONSENT_SCRIPT']}")
    consent = input("🎤 Patient (Say 'agree' or 'opt out'): ")

    if consent.lower() == "opt out":
        print("🤖 Call terminated. Connecting to human operator...")
        return

    print("\n✅ Consent Recorded. Session Started.")
    print("(Type 'escalate' to test handoff, 'quit' to end)")

    while True:
        user_input = voice.listen()
        if user_input.lower() in ["quit", "exit"]:
            print("🤖 Thank you. Call ended.")
            break
        if user_input.lower() == "escalate":
            bot._escalate_to_human("User requested human", "Manual Escalation")
            break

        response = bot.handle_query(user_input, phone="9876543210")
        voice.speak(response)

if __name__ == "__main__":
    # Check API Key
    if not CONFIG["DEEPSEEK_API_KEY"] or CONFIG["DEEPSEEK_API_KEY"] == "":
        print("❌ Error: Please set DEEPSEEK_API_KEY in .env file.")
        print("   Create a .env file with: DEEPSEEK_API_KEY=sk-your-key")
    else:
        run_poc()
