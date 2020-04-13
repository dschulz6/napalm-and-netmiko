#! /usr/bin/env python
"""
open acl merge file
compare to current acl's 
add acl entries if needed
print additions to screen

"""
import json
from napalm import get_network_driver

driver = get_network_driver('ios')
iosv = driver('192.168.0.200', 'Qwest', 'ilfnb980')
iosv.open()

# compare acls from a file and merge
print ("Accessing 192.168.0.200")
iosv.load_merge_candidate(filename='acl_cfg_merge.txt')

diffs = iosv.compare_config()
if len(diffs) > 0:
	print(diffs)
	iosv.commit_config()
else:
    print ("No changes required. ")
    iosv.discard_config()

iosv.close()



