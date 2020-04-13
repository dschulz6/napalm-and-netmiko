# this script:
#      logs in to a router
#      does a show ip interface brief
#      

from netmiko import ConnectHandler
from getpass import getpass

iosv_l2 = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.200',
	'username': 'Qwest',
	'password': getpass()
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('sh ip int brief')
print (output)

#for n in range (2,21):
#    print ("Creating VLAN " + str(n))
#    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
#    output = net_connect.send_config_set(config_commands)
#    print (output)
