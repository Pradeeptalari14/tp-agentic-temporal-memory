#!/usr/bin/env bash
set -eo pipefail

echo "=========================================================="
echo "⚡ Validating Agentic Temporal Memory & Episodic Graph"
echo "=========================================================="

python3 -m py_compile temporal_memory_engine.py
echo "✓ temporal_memory_engine.py syntax validated."

python3 -m py_compile manim_flow.py
echo "✓ manim_flow.py syntax validated."

python3 -c "
from temporal_memory_engine import TemporalMemoryManager
mgr = TemporalMemoryManager()
mgr.insert_fact('fact-1', 'AppServer', 'RUNS_PORT', '8080')
ctx = mgr.retrieve_active_context()
assert len(ctx) == 1, 'Fact retrieval mismatch'
print('✓ Unit verification passed: Temporal memory insert/retrieve clean.')
"

echo "=========================================================="
echo "✅ All SRE validation checks passed successfully!"
echo "=========================================================="
