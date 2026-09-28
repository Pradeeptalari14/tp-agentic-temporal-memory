"""
Autonomous Agent Temporal Memory & Episodic Graph Engine
Dual vector-graph storage with exponential Ebbinghaus memory decay and consolidation.
"""
from typing import Dict, List, Any
import math
import time

class MemoryFact:
    def __init__(self, fact_id: str, entity: str, relation: str, value: str, timestamp: float):
        self.fact_id = fact_id
        self.entity = entity
        self.relation = relation
        self.value = value
        self.timestamp = timestamp
        self.rehearsal_count = 1

    def compute_retention(self, current_time: float, decay_rate: float = 0.05) -> float:
        # Ebbinghaus exponential forgetting curve: R = e^(-t / S)
        elapsed_days = (current_time - self.timestamp) / 86400.0
        stability = 1.0 + (self.rehearsal_count * 0.8)
        retention = math.exp(-decay_rate * elapsed_days / stability)
        return round(retention, 4)

class TemporalMemoryManager:
    def __init__(self):
        self.graph_store: Dict[str, MemoryFact] = {}

    def insert_fact(self, fact_id: str, entity: str, relation: str, value: str):
        now = time.time()
        if fact_id in self.graph_store:
            self.graph_store[fact_id].rehearsal_count += 1
            self.graph_store[fact_id].timestamp = now
        else:
            self.graph_store[fact_id] = MemoryFact(fact_id, entity, relation, value, now)

    def retrieve_active_context(self, min_retention: float = 0.4) -> List[Dict[str, Any]]:
        now = time.time()
        active = []
        for f in self.graph_store.values():
            score = f.compute_retention(now)
            if score >= min_retention:
                active.append({
                    "entity": f.entity,
                    "relation": f.relation,
                    "value": f.value,
                    "retention": score
                })
        return active

if __name__ == "__main__":
    mgr = TemporalMemoryManager()
    mgr.insert_fact("f1", "Production_DB", "USES_PASSWORDLESS_AUTH", "Vault-Transit")
    mgr.insert_fact("f2", "User_Preference", "FAVORS_FRAMEWORK", "FastAPI")
    ctx = mgr.retrieve_active_context()
    print("Retrieved Active Facts:", len(ctx), ctx)
