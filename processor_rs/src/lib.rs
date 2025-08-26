
use pyo3::prelude::*;

fn step_core(state: &[f32]) -> Vec<f32> {
    let n = state.len();
    let mut out: Vec<f32> = vec![0.0; n];
    for i in 0..n {
        let xi = state[i];
        let left = state[(i + n - 1) % n];
        let right = state[(i + 1) % n];
        out[i] = 0.92 * xi + 0.04 * left + 0.04 * right + 0.001 * (i as f32);
    }
    out
}

#[pyfunction]
fn step(state: Vec<f32>) -> PyResult<Vec<f32>> {
    Ok(step_core(&state))
}

#[pyfunction]
fn roll_out(mut state: Vec<f32>, steps: usize) -> PyResult<Vec<f32>> {
    for _ in 0..steps {
        state = step_core(&state);
    }
    Ok(state)
}

#[pymodule]
fn processor_rs(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(step, m)?)?;
    m.add_function(wrap_pyfunction!(roll_out, m)?)?;
    Ok(())
}
