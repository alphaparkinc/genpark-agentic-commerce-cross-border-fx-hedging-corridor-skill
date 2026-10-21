# -*- coding: utf-8 -*-
"""Cross-Border FX Hedging Corridor for GenPark Agentic Commerce."""
import json
import math
from typing import Dict, Any

class CrossBorderFXHedgingNettingCorridor:
    @staticmethod
    def calculate_fx_value_at_risk(unhedged_exposure_base_currency: float, currency_pair: str, historical_volatility_pct: float = 8.5, horizon_days: int = 30) -> Dict[str, Any]:
        # 95% confidence Z-score = 1.645
        # VaR = Exposure * Volatility * sqrt(horizon/365) * 1.645
        daily_vol = (historical_volatility_pct / 100.0) / math.sqrt(365.0)
        horizon_vol = daily_vol * math.sqrt(horizon_days)
        var_usd = round(unhedged_exposure_base_currency * horizon_vol * 1.645, 2)
        var_pct = round((var_usd / unhedged_exposure_base_currency) * 100.0, 2)
        
        recommendation = "ENTER_FORWARD_COLLAR" if var_pct > 3.0 else "UNHEDGED_MONITORING"
        return {
            "currency_pair": currency_pair,
            "exposure_usd": unhedged_exposure_base_currency,
            "horizon_days": horizon_days,
            "95pct_value_at_risk_usd": var_usd,
            "var_pct_of_portfolio": var_pct,
            "treasury_action": recommendation
        }

    @staticmethod
    def synthesize_forward_contract_netting_plan(receivables_usd: float, payables_eur: float, eur_usd_spot: float = 1.08) -> Dict[str, Any]:
        payables_usd_equiv = round(payables_eur * eur_usd_spot, 2)
        net_exposure_usd = round(receivables_usd - payables_usd_equiv, 2)
        spread_savings_usd = round(min(receivables_usd, payables_usd_equiv) * 0.015, 2)
        
        return {
            "receivables_usd": receivables_usd,
            "payables_eur": payables_eur,
            "payables_usd_equivalent": payables_usd_equiv,
            "net_surplus_deficit_usd": net_exposure_usd,
            "intercompany_netting_fx_spread_savings_usd": spread_savings_usd,
            "hedging_instruction": f"Book 60-day forward contract for net {abs(net_exposure_usd)} USD."
        }
