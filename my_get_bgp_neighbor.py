#! /usr/bin/env python
"""
ssh to router 
display bgp neighbor info to screen

"""
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosv = driver('192.168.0.200', 'Engineer', 'ilfnb980')
iosv.open()

ios_output = iosv.get_facts()

bgp_neighbors = iosv.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))

iosv.close()

