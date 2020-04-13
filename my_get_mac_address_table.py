#! /usr/bin/env python
"""
- ssh to a router
- get mac address table 

"""
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2 = driver('192.168.0.200', 'Qwest', 'ilfnb980')
iosvl2.open()

ios_output = iosvl2.get_mac_address_table()
print (json.dumps(ios_output, indent=4))
