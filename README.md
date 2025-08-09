# 📊 Bayesian Time-Series Regime-Change Analysis of Brent Crude Oil Prices

## Problem Statement
Brent crude oil prices exhibit long stretches of “regimes” (e.g., stable uptrends, crashes, high-volatility plateaus) that are often linked to real-world shocks: OPEC/OPEC+ decisions, wars/sanctions, infrastructure outages, or global demand collapses. Traditional averages blur those structural breaks. We need a workflow that:
- Treats **prices as a time series**, not independent points,
- **Detects and interprets regime changes**, and
- Grounds interpretation with a curated list of **historical events**.

This repository implements that workflow in stages. **Task 1** focuses on high-quality data intake and exploratory analysis to prepare for Bayesian regime-change modeling (Task 2) and visualization (Task 3).

---

## 🎯 Project Overview

- **Goal:**  
  Identify regime changes in the daily log-returns of Brent crude oil prices via a Bayesian change-point model (PyMC3) and visualize with an interactive dashboard.

- **Tasks:**  
  1. **🧪 Task 1 – EDA & Workflow**  
     - Load & clean the raw price time-series  
     - Visualize prices & log-returns  
     - Compile 10–15 key events in `events.csv`  
     - Document assumptions & workflow in a Jupyter notebook  
  2. **🧠 Task 2 – Bayesian Modeling**  
     - Specify discrete uniform prior for change-point τ  
     - Define pre/post regime means (μ₁, μ₂) & shared σ  
     - Sample posterior with PyMC3 and summarize results  
     - (Optional) Extend with covariates or Markov-switching models  
  3. **📈 Task 3 – Interactive Dashboard**  
     - **Backend:** Flask API serving price series & regime dates  
     - **Frontend:** React app (Recharts/Chart.js) highlighting regimes  

---

## 🗂️ Folder Structure

```
bayesian_time_series_regime_change_analysis/
├── README.md
├── requirements.txt            # Python dependencies
├── configs/
│   └── config.yml             # Configuration parameters
├── data/
│   ├── BrentOilPrices.csv     # Raw daily Brent crude oil prices
│   ├── events_compiled.csv    # Compiled geopolitical/OPEC events
│   └── reports/               # Data analysis outputs
├── docs/
│   └── WORKFLOW.md            # Detailed workflow documentation
├── notebooks/
│   └── 1_time_series_EDA_and_Workflow.ipynb
└── reports/
    └── figures/               # Generated plots and visualizations
```

- **configs/**  
  - `config.yml`: Project configuration and parameters  

- **data/**  
  - `BrentOilPrices.csv`: Historical Brent crude oil price data  
  - `events_compiled.csv`: Curated list of key geopolitical/OPEC events with dates  
  - `reports/`: Data processing outputs and intermediate results  

- **docs/**  
  - `WORKFLOW.md`: Comprehensive workflow and methodology documentation  

- **notebooks/**  
  - `1_time_series_EDA_and_Workflow.ipynb`: Exploratory data analysis, visualizations, and workflow documentation  

- **reports/**  
  - `figures/`: Generated charts, plots, and statistical visualizations  

---

## 📋 Project Status

### ✅ Completed
- **Task 1 - EDA & Workflow**: 
  - ✅ Data loading and cleaning pipeline
  - ✅ Comprehensive exploratory data analysis
  - ✅ Time series visualizations (price series, log returns, decomposition)
  - ✅ Statistical analysis (ACF, PACF, rolling statistics)
  - ✅ Event compilation and data integration
  - ✅ Workflow documentation

### 🚧 In Progress
- **Task 2 - Bayesian Modeling**: Planned implementation of change-point detection
- **Task 3 - Interactive Dashboard**: Planned development of web interface

---

## ⚙️ Getting Started

1. **🚀 Clone the repo**  
   ```bash
   git clone <your-repo-url>
   cd bayesian_time_series_regime_change_analysis
````

2. **🛠 Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

   Or install manually:
   ```bash
   pip install pandas numpy matplotlib statsmodels scipy pyyaml jupyterlab ipywidgets
   # PyMC3 & extras will be needed for Task 2
   pip install pymc3 arviz
   ```

3. **📂 Data Setup**

   The project includes:
   * `data/BrentOilPrices.csv`: Historical Brent crude oil price data
   * `data/events_compiled.csv`: Curated geopolitical/OPEC events with dates
   * `configs/config.yml`: Configuration parameters for analysis

4. **▶️ Run Task 1 notebook**

   ```bash
   jupyter lab notebooks/1_time_series_EDA_and_Workflow.ipynb
   ```

5. **📊 View Generated Outputs**

   After running the notebook, you'll find:
   - **Visualizations**: `reports/figures/` contains all generated plots
   - **Statistical Analysis**: ACF/PACF plots, rolling statistics, STL decomposition
   - **Event Analysis**: Price series with major events highlighted
   - **Data Reports**: CSV files with top/bottom price movements

6. **📖 Documentation**

   - Review `docs/WORKFLOW.md` for detailed methodology
   - Check `configs/config.yml` for analysis parameters

5. **➡️ Next Steps**

   * **Task 2**: Implement Bayesian change-point modeling with PyMC3
   * **Task 3**: Build interactive dashboard (Flask + React)
   * Review generated visualizations in `reports/figures/`
   * Explore event correlations and statistical insights

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or submit an issue for enhancements.

---

## 📄 License

This project is licensed under the MIT License.

```

