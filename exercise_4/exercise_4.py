
# Defining templates
access_template = ["switchport mode access", "switchport access vlan {}","switchport nonegotiate", "spanning-tree portfast",
"spanning-tree bpduguard enable"]

trunk_template = ["switchport trunk encapsulation dot1q", "switchport mode trunk",
"switchport trunk allowed vlan {}"]

# Requesting input
interface_mode = raw_input("Enter interface mode (access/trunk): ")

interface_type = raw_input("Enter interface type and number: ")

if interface_mode == "access" or interface_mode == "Access" or interface_mode == "ACCESS":
    vlan_number = raw_input("Enter VLAN number ")
    # Printing output...
    print "Interface", interface_type
    print access_template[0]
    print access_template[1].replace("{}",vlan_number)
    print access_template[2]
    print access_template[3]
    print access_template[4]

elif interface_mode == "trunk" or interface_mode == "Trunk" or interface_mode == "TRUNK":
    allowed_vlans = raw_input("Enter allowed VLANs: ")
    # Printing output...
    print "Interface", interface_type
    print trunk_template[0]
    print trunk_template[1]
    print trunk_template[2].replace("{}", allowed_vlans)
else:
    print "Interface mode not supported"


