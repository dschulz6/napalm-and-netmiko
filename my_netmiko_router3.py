# this script:
#      prompts the user for name and password
#      opens a file called commands_list
#      opens a file called devices_list
#      logs in to each router in the list
#      (this script adds exception handling !!)
#      (this version adds a check for device type router or switch
#         and executes different commands based on device type)
#      does a show ip interface brief
#      executes the commands from the file
#      one line at a time 

from getpass import getpass
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
from netmiko.ssh_exception import AuthenticationException

# IOS version types
list_versions = ['vios_l2-ADVENTERPRISEK9-M',
                 'vios-ADVENTERPRISEK9-M',
                 'C2900-UNIVERSALK9-M',
                 'C3750-ADVIPSERVICESK9-M'
                 ]


with open('commands_file.txt') as f:
	commands_list_switch = f.read().splitlines()

with open('commands_file.txt') as f:
    commands_list_router = f.read().splitlines()    

with open('devices_file.txt') as f:
	devices_list = f.read().splitlines()	

for devices in devices_list:
	print ("Connecting to device " + devices)
	ip_address_of_device = devices
	ios_device = {
	    'device_type': 'cisco_ios',
	    'ip': ip_address_of_device,
	    'username': 'Qwest',
	    'password': getpass()
    }

try:
    net_connect = ConnectHandler(**ios_device)
except (AuthenticationException):
    print ("Authentication failure: " + ip_address_of_device)
except (NetMikoTimeoutException):
    print ("Timeout to device: " + ip_address_of_device)
except (EOFError):
    print ("End of file while attempting " + ip_address_of_device)
except (SSHExcecption):
    print ("SSH Issue. Are you sure SSH i" + ip_address_of_device)
except Exception as unknown_error:
    print ("Some other error: " + unknown_error)

for software_ver in list_versions:
    print ("Checking for " + software_ver)
    output_version = net_connect.send_command('show version')
    int_version = 0 # Reset integer value
    int_version = output_version.find(software_ver) # Check software ver
    if int_version > 0:
        print ("Software version found: " + software_ver)
        break
    else:
        print ("Did not find " + software_ver)

if software_ver == 'vios-ADVENTERPRISEK9-M':
    print ("Running " + software_ver + "commands ")
    output = net_connect.send_config_set(commands_list_switch)
elif software_ver == 'C2900-UNIVERSALK9-M':
    print ("Running " + software_ver + "commands ")
    output = net_connect.send_config_set(commands_list_router)
print (output)    
                        
