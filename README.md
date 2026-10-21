# Cross-Border Multi-Currency FX Hedging & Netting Corridor Skill

[![GenPark Official](https://img.shields.io/badge/GenPark-Official%20Skill-blue)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-blue)](https://www.linkedin.com/company/92955550)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-green)](https://modelcontextprotocol.io/)
[![Zero Dependency](https://img.shields.io/badge/Dependencies-Zero%20Stdlib-brightgreen)](https://python.org)

Rolling forward contract scheduler, value-at-risk (VaR) fx exposure, multi-currency cash flow netting, and slippage tolerance. Built for GenPark (https://www.genpark.ai).

## 🌐 Official Channels
- **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550)

## 🛠️ MCP Tools Exposed
- `calculate_fx_value_at_risk`: Calculate 95% Parametric FX Value-at-Risk (VaR) on unhedged multi-currency receivables.
- `synthesize_forward_contract_netting_plan`: Net cross-border payables and receivables across EUR, GBP, JPY, and USD to minimize bank conversion spreads.

## 🚀 Installation & Usage
```bash
python -m genpark_agentic_commerce_cross_border_fx_hedging_corridor_skill.server --test
```
