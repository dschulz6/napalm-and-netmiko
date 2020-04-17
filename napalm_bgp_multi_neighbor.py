import json
from napalm import get_network_driver

bgplist = ['192.168.0.200',
           '192.168.0.202'
           ]

for ip_address in bgplist:
    print ("Connecting to " + str(ip_address))
    driver = get_network_driver('ios')
    iosv_router = driver(ip_address, 'Engineer', 'ilfnb980')
    iosv_router.open()
    bgp_neighbors = iosv_router.get_bgp_neighbors()
    print (json.dumps(bgp_neighbors, indent=4))
    iosv_router.close           

ios_output = iosv.get_facts()

bgp_neighbors = iosv.get_bgp_neighbors()
print (json.dumps(bgp_neighbors, indent=4))

iosv.close()


