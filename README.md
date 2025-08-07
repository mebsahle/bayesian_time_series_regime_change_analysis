# 📊 Bayesian Time-Series Regime-Change Analysis of Brent Crude Oil Prices

A comprehensive repo to detect structural breaks in Brent crude oil prices using Bayesian change-point modeling and link them to key geopolitical/OPEC events.

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

bayesian\_time\_series\_regime\_change\_analysis/
├── README.md
├── data/
│   ├── brent\_prices.csv       # Raw daily prices (Date, Price)
│   └── events.csv             # Key events (event, start\_date)
└── notebooks/
└── 1\_time\_series\_EDA\_and\_Workflow\.ipynb

````

- **data/**  
  - `brent_prices.csv`: Historical Brent prices  
  - `events.csv`: 10–15 geopolitical/OPEC event dates  

- **notebooks/**  
  - `1_time_series_EDA_and_Workflow.ipynb`: EDA, visualizations, events loading, and workflow documentation  

---

## ⚙️ Getting Started

1. **🚀 Clone the repo**  
   ```bash
   git clone <your-repo-url>
   cd bayesian_time_series_regime_change_analysis
````

2. **🛠 Install dependencies**

   ```bash
   pip install pandas numpy matplotlib
   # PyMC3 & extras will be needed for Task 2
   pip install pymc3 arviz
   ```

3. **📂 Prepare data**

   * Place your Brent price CSV at `data/brent_prices.csv`
   * Fill in `data/events.csv` with your chosen events

4. **▶️ Run Task 1 notebook**

   ```bash
   jupyter lab notebooks/1_time_series_EDA_and_Workflow.ipynb
   ```

5. **➡️ Next Steps**

   * Proceed to **Task 2** (modeling)
   * Then build the **Task 3** dashboard

---

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!
Feel free to open a pull request or submit an issue for enhancements.

---

## 📄 License

This project is licensed under the MIT License.

```

