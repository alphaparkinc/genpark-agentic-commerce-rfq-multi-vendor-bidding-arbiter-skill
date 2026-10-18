#!/usr/bin/env python3
import json
import sys
from client import AgenticCommerceRFQMultiVendorArbiter

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--test":
        arbiter = AgenticCommerceRFQMultiVendorArbiter()
        rfq = {"part_number": "MCU-ARM-C9", "target_quantity": 2000, "max_unit_budget": 12.0}
        bids = [
            {"vendor_name": "Foxconn Precision", "unit_price_usd": 10.50, "moq": 1000, "shipping_cost_usd": 400.0, "payment_terms_days": 60, "quality_rating_pct": 98.0},
            {"vendor_name": "Shenzhen FastPCB", "unit_price_usd": 9.80, "moq": 3000, "shipping_cost_usd": 700.0, "payment_terms_days": 15, "quality_rating_pct": 91.0}
        ]
        res = arbiter.arbitrate_vendor_bids(rfq, bids)
        assert res["winning_vendor"]["vendor_name"] == "Foxconn Precision"
        assert res["winning_vendor"]["within_budget"] is True
        print(f"[TEST PASS] RFQ Arbiter Winner: {res['winning_vendor']['vendor_name']}")
        sys.exit(0)

    for line in sys.stdin:
        if not line.strip():
            continue
        try:
            req = json.loads(line)
            method = req.get("method")
            msg_id = req.get("id")
            if method == "initialize":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"serverInfo": {"name": "genpark-rfq-arbiter", "version": "1.0.0"}}}))
            elif method == "tools/list":
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"tools": [{"name": "arbitrate_vendor_bids", "description": "Arbitrate multi-vendor RFQ bids and select optimal supplier"}]}}))
            elif method == "tools/call":
                args = req.get("params", {}).get("arguments", {})
                arbiter = AgenticCommerceRFQMultiVendorArbiter()
                out = arbiter.arbitrate_vendor_bids(args.get("rfq_spec", {}), args.get("vendor_bids", []))
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "result": {"content": [{"type": "text", "text": json.dumps(out)}]}}))
            else:
                print(json.dumps({"jsonrpc": "2.0", "id": msg_id, "error": {"code": -32601, "message": "Method not found"}}))
            sys.stdout.flush()
        except Exception as e:
            print(json.dumps({"jsonrpc": "2.0", "error": {"code": -32603, "message": str(e)}}))
            sys.stdout.flush()

if __name__ == "__main__":
    main()
