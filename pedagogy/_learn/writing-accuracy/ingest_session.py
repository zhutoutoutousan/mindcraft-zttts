#!/usr/bin/env python3
"""CLI wrapper: ingest a writing-accuracy session into lexicon + bridge graphs.

  python pedagogy/_learn/writing-accuracy/ingest_session.py --session pedagogy/_learn/writing-accuracy/sessions/FILE.toon.md
"""
from __future__ import annotations

import runpy
import sys
from pathlib import Path

HOOK = Path(__file__).resolve().parents[3] / ".cursor" / "hooks" / "polyglot_ingest.py"
sys.argv[0] = str(HOOK)
runpy.run_path(str(HOOK), run_name="__main__")
