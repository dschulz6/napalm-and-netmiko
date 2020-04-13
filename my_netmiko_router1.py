# this script:
#      opens a file called commands_file
#      logs in to a router
#      does a show ip interface brief
#      executes the CONFIGURATION commands from the file
#      one line at a time 

from netmiko import ConnectHandler
from getpass import getpass

with open('commands_file.txt') as f:
	commands_to_send = f.read().splitlines()

ios_devices = {
	'device_type': 'cisco_ios',
	'ip': '192.168.0.200',
	'username': 'Qwest',
	'password': getpass()
}

all_devices = [ios_devices]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_command("sh ip int brief")
    print(output)
    output = net_connect.send_config_set(commands_to_send)
    print (output)

#for n in range (2,21):
#    print ("Creating VLAN " + str(n))
#    config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
#    output = net_connect.send_config_set(config_commands)
#    print (output)
