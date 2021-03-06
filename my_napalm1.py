# this script logs into a router and gets the following
# info formatted in json:
#     device facts
#     device interfaces
#     device interface counters 
#
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosvl2 = driver('192.168.0.202', 'Engineer', 'ilfnb980')
iosvl2.open()

ios_output = iosvl2.get_facts()
print (json.dumps(ios_output, indent=4))

ios_output = iosvl2.get_interfaces()
print (json.dumps(ios_output, sort_keys=True, indent=4))

ios_output = iosvl2.get_interfaces_counters()
print (json.dumps(ios_output, sort_keys=True, indent=4))
