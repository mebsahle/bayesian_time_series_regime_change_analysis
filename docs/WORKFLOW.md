# Task 1 Workflow (Living Document)

1. Intake & Validation → schema, date parsing, duplicates, missingness.
2. Transformations → sort by date, forward-fill small gaps, compute log-returns.
3. Visuals → price series, log-returns, rolling mean/std, histograms, ACF/PACF.
4. Diagnostics → ADF test, optional STL decomposition/resampling.
5. Event Overlay → vertical lines for `events.csv` dates.
6. Notes & Assumptions → document choices and caveats.