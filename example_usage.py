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
