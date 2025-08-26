from __future__ import annotations
from typing import Dict, Any
import numpy as np

try:
    import processor_rs  # Rust extension via PyO3
except Exception as e:  # pragma: no cover
    processor_rs = None
    _IMPORT_ERROR = e
else:
    _IMPORT_ERROR = None

from .encoder import encode_observations
from .decoder import decode_state

def run_pipeline(obs: Dict[str, Any], steps: int = 5):
    if processor_rs is None:
        raise RuntimeError(f"Rust extension not available: {_IMPORT_ERROR}")
    state0 = encode_observations(obs)
    state_final = processor_rs.roll_out(state0.tolist(), steps)
    return decode_state(np.asarray(state_final, dtype=float))
