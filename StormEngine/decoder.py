from __future__ import annotations
from typing import Dict, Any
import numpy as np

def decode_state(state: np.ndarray) -> Dict[str, Any]:
    state = np.asarray(state, dtype=float)
    t_n, u_n, v_n, p_n = (state[0], state[1], state[2], state[3])
    temperature = 290.0 + 20.0 * t_n
    wind_u = 20.0 * u_n
    wind_v = 20.0 * v_n
    pressure = 1013.0 + 50.0 * p_n
    return {
        "temperature_K": float(temperature),
        "wind_u_ms": float(wind_u),
        "wind_v_ms": float(wind_v),
        "pressure_hPa": float(pressure),
    }
