
from netaddr import *
import pprint

# Function to verify if an ip address is correct


def validate_ip(s):
    a = s.split('.')
    if len(a) != 4:
        return 0
    for x in a:
        if not x.isdigit():
            return 0
        i = int(x)
        if i < 0 or i > 255:
            return 0
    return 1

# Function to verify a IP mask


def validate_mask(s):
    a = s.split('/')
    if len(a) != 2:
        return 0
    if not a[1].isdigit():
        return 0
    i = int(a[1])
    if i < 0 or i > 32:
        return 0
    return 1


# Requesting an ip address and mask

ip_address = raw_input("Enter Ip address: ")

ip_mask = raw_input("Enter subnet mask in decimal format: ")


# While the ip and mask are invalid, I still requesting them

while validate_ip(ip_address) == 0:
    print ("Invalid IP address format")
    ip_address = raw_input("Enter Ip address: ")

while validate_mask(ip_mask) == 0:
    print ("Subnet mask is invalid")
    ip_mask = raw_input("Enter subnet mask in decimal format: ")

# Using netaddr to get the broadcast ,network IP address and the IP address in bits
ip_address_bits = IPAddress(ip_address)
ip_with_mask = IPNetwork(ip_address+ip_mask)
ip_network = ip_with_mask.network
ip_broadcast = ip_with_mask.broadcast
splitted_ip = str(ip_address).split('.')


# Printing output...
print ("     " + splitted_ip[0] + "       " + splitted_ip[1] + "       " + splitted_ip [2] + "       " + splitted_ip[3])
print ip_address_bits.bits()
print ("network address is: "+str(ip_network))
print ("broadcast address is: "+str(ip_broadcast))
