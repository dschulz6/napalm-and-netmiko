import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosv = driver('192.168.0.200', 'Engineer', 'ilfnb980')
iosv.open()

# compare acls and bgp configs from files
print ("Accessing 192.168.0.200")
iosv.load_merge_candidate(filename='acl1.cfg')

diffs = iosv.compare_config()
if len(diffs) > 0:
	print(diffs)
	
else:
    print ("No acl changes required. ")
    iosv.discard_config()

print ("Accessing 192.168.0.200")
iosv.load_merge_candidate(filename='bgp.cfg')

diffs = iosv.compare_config()
if len(diffs) > 0:
	print(diffs)
	
else:
    print ("No bgp changes required. ")
    iosv.discard_config()    

iosvl2.close()


