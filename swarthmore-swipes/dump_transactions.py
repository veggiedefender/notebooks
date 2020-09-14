#!/usr/bin/env python3
import json
import sys
import cbord_api

try:
    device_id = sys.argv[1]
    pin = sys.argv[2]
except IndexError:
    print('Usage: python3 dump_transactions.py <device_id> <pin>')
    sys.exit(1)

session_id = cbord_api.authenticate(device_id, pin)
transactions = cbord_api.get_transactions(session_id)

sys.stdout.write(json.dumps(transactions, sort_keys=True, indent=2))
