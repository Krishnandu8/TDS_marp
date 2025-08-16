# analysis.py
# Author email: 24ds2000075@ds.study.iitm.ac.in

import marimo as mo

app = mo.App()

@app.cell
def __(mo):
    """
    Data source cell
    - Generates a simple synthetic dataset with a linear relationship plus noise.
    - Outputs: df (DataFrame with columns 'x' and 'y')
    Downstream: Transform/summary cells depend on df.
    """
    import numpy as np
    import pandas as pd

    rng = np.random.default_rng(42)
    n = 200
    x = np.linspace(0, 10, n)
    y = 2.0 * x + 5 + rng.normal(0, 3, n)

    df = pd.DataFrame({"x": x, "y": y})
    return df

@app.cell
def __(mo):
    """
    UI control cell
    - Provides an interactive slider that controls the smoothing window.
    - Outputs: slider (widget), use slider.value downstream.
    Downstream: Transform/summary cells depend on slider.value.
    """
    # Odd window sizes are common for centered rolling operations
    slider = mo.ui.slider(3, 51, value=11, step=2, label="Smoothing window (odd)")
    return slider

@app.cell
def __(df, slider, mo):
    """
    Transform & summary cell
    - Depends on: df (data), slider.value (control).
    - Computes a smoothed version of y and the Pearson correlation between x and smoothed y.
    - Produces dynamic Markdown that updates reactively when the slider changes.
    Outputs: smoothed (Series), corr (float), report (Markdown UI object).
    """
    window = slider.value

    # Smooth the y signal with a centered rolling mean
    smoothed = df["y"].rolling(window=window, min_periods=1, center=True).mean()

    # Relationship metric: correlation between x and smoothed y
    corr = df["x"].corr(smoothed)

    # Human-readable strength bucket + simple visual bar
    strength_labels = ("very weak", "weak", "moderate", "strong", "very strong")
    idx = min(int(abs(corr) / 0.2), 4)
    bar = "🟩" * (idx + 1) + "⬜" * (5 - (idx + 1))

    report = mo.md(
        f"""
### Relationship summary

- Window size: **{window}**
- Pearson correlation between x and smoothed y: **{corr:.3f}**
- Strength: **{strength_labels[idx]}** {bar}

> Move the slider to change smoothing and see how the correlation responds.
"""
    )

    return smoothed, corr, report

@app.cell
def __(report):
    """
    Presentation cell
    - Depends on: report (Markdown UI object).
    - Purpose: Render dynamic Markdown as visible output.
    """
    report

if __name__ == "__main__":
    # Edit mode: uvx marimo edit analysis.py
    app.run()
