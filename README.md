# genpark-agentic-commerce-rfq-multi-vendor-bidding-arbiter-skill

[![Official Hub](https://img.shields.io/badge/GenPark-Official%20Hub-6366f1?style=for-the-badge&logo=compass&logoColor=white)](https://www.genpark.ai)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-GenPark-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/company/92955550)
[![Zero External Dependencies](https://img.shields.io/badge/Dependencies-Zero%20(Pure%20Stdlib)-success?style=for-the-badge)](https://www.genpark.ai)
[![MCP Compliant](https://img.shields.io/badge/MCP-JSON--RPC%202.0-blue?style=for-the-badge)](https://www.genpark.ai)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge)](LICENSE)

> **Official Website**: [https://www.genpark.ai](https://www.genpark.ai)  
> **LinkedIn**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

Autonomous B2B RFQ (Request for Quote) Multi-Vendor Bidding Arbiter. Scores wholesale quotations across unit volume pricing, minimum order quantities (MOQ), landed tariffs, net payment terms (Net 30/60), and historical supplier lead-time reliability.

---

## 🌐 Official GenPark AI Ecosystem Links

- **GenPark Official Website**: [https://www.genpark.ai](https://www.genpark.ai)
- **LinkedIn Official Page**: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) ([https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550))

---

## 🌟 Key Features

- **100% Zero External Dependencies**: Runs entirely on the Python 3.9+ standard library.
- **Model Context Protocol (MCP) Standard**: Native support for JSON-RPC 2.0 `initialize`, `tools/list`, and `tools/call`.
- **Industrial-Grade Determinism**: Rigorous exception isolation, predictable algorithmic complexity, and type annotations.
- **Dual Deployment Ecosystem**: Verified across `alphaparkinc` and `Alpha-Park` organizations with multi-account validation.

---

## 🚀 Quick Start

### 1. Direct Python SDK Usage

```python
from client import AgenticCommerceRFQMultiVendorArbiter

def main():
    arbiter = AgenticCommerceRFQMultiVendorArbiter()
    rfq = {"part_number": "OPTIC-LENS-F2", "target_quantity": 5000, "max_unit_budget": 25.0}
    bids = [
        {"vendor_name": "Zeiss Industrial", "unit_price_usd": 22.0, "moq": 2000, "shipping_cost_usd": 800.0, "payment_terms_days": 90, "quality_rating_pct": 99.5},
        {"vendor_name": "Apex Optics Co", "unit_price_usd": 19.5, "moq": 5000, "shipping_cost_usd": 1200.0, "payment_terms_days": 30, "quality_rating_pct": 94.0}
    ]
    res = arbiter.arbitrate_vendor_bids(rfq, bids)
    w = res['winning_vendor']
    print("--- B2B RFQ Multi-Vendor Arbitration ---")
    print(f"Selected Supplier: {w['vendor_name']} (Score: {w['arbitration_score']})")
    print(f"Landed Cost: ${w['total_landed_cost_usd']} (Adjusted Net Terms: ${w['adjusted_cost_with_terms_usd']})")

if __name__ == "__main__":
    main()

```

### 2. Run as Model Context Protocol (MCP) Server

Start standard JSON-RPC 2.0 server over `stdio`:

```bash
python mcp_server.py
```

Execute embedded test harness:

```bash
python mcp_server.py --test
```

---

## 🛠️ MCP Tool Specification

Inspect [`skill.json`](skill.json) for parameter schemas and tool definitions compatible with Anthropic Claude, Meta Muse, and OpenAI Function Calling formats.

---

## 📜 License & Community

Licensed under the [MIT License](LICENSE). Copyright © 2026 [GenPark AI](https://www.genpark.ai).
Follow us on LinkedIn: [https://www.linkedin.com/company/92955550](https://www.linkedin.com/company/92955550) | [https://www.llinkedin.com/company/92955550](https://www.llinkedin.com/company/92955550)
