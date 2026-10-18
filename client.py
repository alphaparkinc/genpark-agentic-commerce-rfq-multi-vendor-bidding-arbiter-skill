"""
Agentic Commerce RFQ Multi-Vendor Arbiter (Pure Stdlib)
Official Website: https://www.genpark.ai | LinkedIn: https://www.llinkedin.com/company/92955550
"""
from typing import Dict, Any, List

class AgenticCommerceRFQMultiVendorArbiter:
    def __init__(self, arbiter_name: str = "GenPark-RFQ-Bidding-Core"):
        self.arbiter_name = arbiter_name

    def arbitrate_vendor_bids(self, rfq_spec: Dict[str, Any], vendor_bids: List[Dict[str, Any]]) -> Dict[str, Any]:
        qty = int(rfq_spec.get("target_quantity", 1000))
        max_budget = float(rfq_spec.get("max_unit_budget", 50.0))
        
        evaluated_bids = []
        for bid in vendor_bids:
            vname = bid.get("vendor_name", "Supplier")
            unit_price = float(bid.get("unit_price_usd", 45.0))
            moq = int(bid.get("moq", 500))
            ship = float(bid.get("shipping_cost_usd", 200.0))
            quality = float(bid.get("quality_rating_pct", 95.0))
            terms = int(bid.get("payment_terms_days", 30))
            
            effective_qty = max(qty, moq)
            total_landed = (unit_price * effective_qty) + ship
            effective_unit_cost = total_landed / effective_qty
            
            # Working capital discount for favorable Net terms (e.g. Net 60 provides 1.5% working capital benefit)
            working_capital_benefit = total_landed * (terms / 365.0) * 0.08
            adjusted_cost = total_landed - working_capital_benefit
            
            # Composite score: Lower cost and higher quality yield higher score
            score = round((quality / 100.0) / (adjusted_cost / 10000.0), 3)
            
            evaluated_bids.append({
                "vendor_name": vname,
                "unit_price_usd": unit_price,
                "effective_order_quantity": effective_qty,
                "total_landed_cost_usd": round(total_landed, 2),
                "adjusted_cost_with_terms_usd": round(adjusted_cost, 2),
                "quality_rating_pct": quality,
                "arbitration_score": score,
                "within_budget": effective_unit_cost <= max_budget
            })
            
        evaluated_bids.sort(key=lambda x: x["arbitration_score"], reverse=True)
        winner = evaluated_bids[0] if evaluated_bids else None
        
        return {
            "arbiter": self.arbiter_name,
            "rfq_part": rfq_spec.get("part_number", "PART-CORE"),
            "evaluated_vendors_count": len(evaluated_bids),
            "winning_vendor": winner,
            "all_ranked_bids": evaluated_bids,
            "verdict": "OPTIMAL_VENDOR_SELECTED"
        }
