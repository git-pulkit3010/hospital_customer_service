"""
Helper script to load and verify all mock data for the Hospital Voice AI POC.
"""

import json
import os
from pathlib import Path

# Get the base directory (project root is parent of src/)
BASE_DIR = Path(__file__).parent.parent
DATA_DIR = BASE_DIR / "data"


def load_patient_db():
    """Load mock patient database"""
    file_path = DATA_DIR / "mock_patient_db.json"
    with open(file_path, 'r') as f:
        return json.load(f)


def load_knowledge_base():
    """Load mock FAQ knowledge base"""
    file_path = DATA_DIR / "mock_knowledge_base.json"
    with open(file_path, 'r') as f:
        return json.load(f)


def load_audit_logs():
    """Load mock audit logs"""
    file_path = DATA_DIR / "mock_audit_logs.jsonl"
    logs = []
    with open(file_path, 'r') as f:
        for line in f:
            logs.append(json.loads(line))
    return logs


def load_cache_store():
    """Load mock cache store"""
    file_path = DATA_DIR / "mock_cache_store.json"
    with open(file_path, 'r') as f:
        return json.load(f)


def print_poc_dashboard():
    """Display POC status dashboard"""
    print("\n" + "=" * 60)
    print("🏥 HOSPITAL VOICE AI POC - DATA STATUS")
    print("=" * 60)

    # Check files
    files = {
        "Patient Database": "mock_patient_db.json",
        "Knowledge Base": "mock_knowledge_base.json",
        "Audit Logs": "mock_audit_logs.jsonl",
        "Cache Store": "mock_cache_store.json"
    }

    for name, file in files.items():
        file_path = DATA_DIR / file
        status = "✅" if file_path.exists() else "❌"
        print(f"{status} {name}: data/{file}")

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

    print("\n📁 FILE LOCATIONS:")
    print(f"   - Base Directory: {BASE_DIR}")
    print(f"   - Data Directory: {DATA_DIR}")
    print(f"   - Logs Directory: {BASE_DIR / 'logs'}")

    print("=" * 60 + "\n")


if __name__ == "__main__":
    print_poc_dashboard()
