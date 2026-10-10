"""Compatibility entry point for the current V35 naval script scenarios.

The former three-axis price simulation described removed systems. Read live
focus/effect/decision/idea code instead. Optional --md/--game provider checks
are forwarded to naval_scenarios.py. These are static tests, not game runtime.
"""
from pathlib import Path
import runpy

if __name__ == "__main__":
    runpy.run_path(str(Path(__file__).with_name("naval_scenarios.py")), run_name="__main__")
