<<<<<<< HEAD
# ProjectGroundStation
=======
# Simplified EPD (Encoder → Processor → Decoder)

A tiny, production-friendly scaffold demonstrating an **encoder-processor-decoder** architecture:
- **Encoder (Python):** turns raw observations into a compact state vector.
- **Processor (Rust via PyO3):** runs a fast autoregressive step `x_{t+1} = A x_t + b` and multi-step rollout.
- **Decoder (Python):** maps the state back into human-friendly predictions.

## Build & Install

```bash
# 1) Ensure Rust and maturin are installed
#    - Rust: https://rustup.rs
#    - maturin: pip install maturin

# 2) From the project root:
maturin develop --release
# or build a wheel:
maturin build --release
```

## Quick Demo

```bash
python examples/run_demo.py
```
>>>>>>> f2125a7 (fisrt Changes)
