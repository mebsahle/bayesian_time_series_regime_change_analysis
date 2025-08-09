from __future__ import annotations
from dataclasses import dataclass
from typing import Optional
import numpy as np
import pandas as pd

@dataclass
class ImpactSummary:
    tau_index: int
    tau_date: str
    pre_price_mean: float
    post_price_mean: float
    price_pct_change: float
    pre_ret_mean: float
    post_ret_mean: float
    ret_mean_diff: float
    pre_ret_std: float
    post_ret_std: float

def compute_returns(df: pd.DataFrame) -> pd.DataFrame:
    out = df.copy()
    out["Price"] = pd.to_numeric(out["Price"], errors="coerce")
    out["Price"] = out["Price"].ffill()
    out["log_ret"] = np.log(out["Price"] / out["Price"].shift(1))
    return out.dropna(subset=["log_ret"])

def summarize_impact(df: pd.DataFrame, tau_idx: int, window_days: Optional[int] = None) -> ImpactSummary:
    if window_days is None:
        pre = df.iloc[:tau_idx]
        post = df.iloc[tau_idx:]
    else:
        tau_date = df.index[tau_idx]
        start = tau_date - pd.Timedelta(days=window_days)
        end = tau_date + pd.Timedelta(days=window_days)
        window = df.loc[start:end]
        pre = window.loc[start:tau_date]
        post = window.loc[tau_date:end]

    pre_price_mean = float(pre["Price"].mean())
    post_price_mean = float(post["Price"].mean())
    price_pct_change = ((post_price_mean - pre_price_mean) / pre_price_mean) * 100.0 if pre_price_mean else float("nan")

    pre_ret = pre["log_ret"]; post_ret = post["log_ret"]
    return ImpactSummary(
        tau_index=int(tau_idx),
        tau_date=str(df.index[tau_idx].date()),
        pre_price_mean=pre_price_mean,
        post_price_mean=post_price_mean,
        price_pct_change=price_pct_change,
        pre_ret_mean=float(pre_ret.mean()),
        post_ret_mean=float(post_ret.mean()),
        ret_mean_diff=float(post_ret.mean() - pre_ret.mean()),
        pre_ret_std=float(pre_ret.std()),
        post_ret_std=float(post_ret.std()),
    )

def nearest_events(tau_date: pd.Timestamp, events: pd.DataFrame, k: int = 3) -> pd.DataFrame:
    ev = events.copy()
    ev["gap_days"] = (ev["start_date"] - tau_date).dt.days.abs()
    return ev.sort_values("gap_days").head(k)

def events_within_window(tau_date: pd.Timestamp, events: pd.DataFrame, window_days: int = 90) -> pd.DataFrame:
    start = tau_date - pd.Timedelta(days=window_days)
    end = tau_date + pd.Timedelta(days=window_days)
    return events[(events["start_date"] >= start) & (events["start_date"] <= end)].copy()
