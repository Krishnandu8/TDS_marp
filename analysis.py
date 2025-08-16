# analysis.py
# Author: 24ds2000075@ds.study.iitm.ac.in

import marimo as mo

app = mo.App()

@app.cell
def __(mo):
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
    slider = mo.ui.slider(3, 51, value=11, step=2, label="Smoothing window (odd)")
    return slider

@app.cell
def __(df, slider, mo):
    smoothed = df["y"].rolling(window=slider.value, min_periods=1, center=True).mean()
    corr = df["x"].corr(smoothed)
    report = mo.md(f"Correlation with smoothing window {slider.value}: **{corr:.3f}**")
    return smoothed, corr, report

@app.cell
def __(report):
    report

if __name__ == "__main__":
    app.run()
