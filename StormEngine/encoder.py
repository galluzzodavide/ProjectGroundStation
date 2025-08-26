from __future__ import annotations
from typing import Dict, Any
import numpy as np

def encode_observations(obs: Dict[str, Any]) -> np.ndarray:
    """Minimal encoder.
    Expected keys: temperature, wind_u, wind_v, pressure.
    """
    t = np.asarray(obs.get("temperature", [290.0]), dtype=float)
    u = np.asarray(obs.get("wind_u", [0.0]), dtype=float)
    v = np.asarray(obs.get("wind_v", [0.0]), dtype=float)
    p = np.asarray(obs.get("pressure", [1013.0]), dtype=float)

    t_n = (t - 290.0) / 20.0
    u_n = u / 20.0
    v_n = v / 20.0
    p_n = (p - 1013.0) / 50.0

    state = np.concatenate([t_n, u_n, v_n, p_n], axis=0).astype(np.float32)
    if state.size < 8:
        state = np.pad(state, (0, 8 - state.size))
    elif state.size > 8:
        state = state[:8]
    return state
