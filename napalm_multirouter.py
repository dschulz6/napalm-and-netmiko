# this script logs into a router and gets the following
# info formatted in json:
#     device facts
#     device interfaces
#     device interface counters 
#
import json
from napalm import get_network_driver

router_r1 = {
	'ip': '192.168.0.200',
	'username': 'Engineer',
	'password': 'ilfnb980'
}

router_r2 = {
	'ip': '192.168.0.202',
	'username': 'Qwest',
	'password': 'ilfnb980'
}

all_devices = [router_r1, router_r2]

for device in all_devices:
    driver = get_network_driver('ios')
    iosvl2 = driver(device["ip"], device["username"], device["password"])
    iosvl2.open()

    ios_output = iosvl2.get_facts()
    print (json.dumps(ios_output, indent=4))

    ios_output = iosvl2.get_interfaces()
    print (json.dumps(ios_output, sort_keys=True, indent=4))

    ios_output = iosvl2.get_interfaces_counters()
    print (json.dumps(ios_output, sort_keys=True, indent=4))
