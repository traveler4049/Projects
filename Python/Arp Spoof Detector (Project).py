"""
Project Task 1: ARP Table Extraction
The first part of the program must handle the extraction of the ARP table data. The data must be saved in a dynamic structure in which the IP address corresponds to the MAC address. The structure is required for later comparison operations, to identify duplicated addresses.
1 Plan a function that will extract the ARP table data from the machine. How can Python access this type of data? How should the data be saved for later use?
2 Import the required modules for the program.
3 Define a function that will handle the ARP table data extraction.
4 Create three variables, one to store the ARP table data, another to store a list of the separated lines, and the third to store the final filtered data.
5 Iterate over the lines and save the IP addresses and their corresponding MAC addresses after data filtration.
Only IP and MAC addresses should be saved in the third variable.
Filter the rest of the data, such as the interface’s IP address or broadcast data.
"""

import os
def arp_table_extraction():
    os.system("arp -a > arp_table.txt")
    with open("arp_table.txt") as arp_file:
        seen_192 = False
        seen_macs = {}
        for line in arp_file:
            line_listed = line.split()
            print (line_listed)
            #print(line[24:41])
            if "Interface: 192.168.1" in line:
                seen_192 = True
                print(seen_192)
            if seen_192 == True and "192.168.1" in line_listed[0]:
                ip_addr = line_listed[0]
                mac_addr = line_listed[1]
                seen_macs[ip_addr] = mac_addr
            print(check_duplicates(seen_macs))




"""Project Task 2: ARP Table Extraction
The second part of the program must take the extracted data and identify if an ARP Spoofing attack is underway.This is done by locating MAC address duplications in the ARP table entries.
1 Plan a function that will identify MAC address duplication.
2 Define a function to identify duplication in MAC addresses. The function should accept a parameter.
3 Create a variable to store iterated MAC addresses for later comparison.
4 Iterate over the recorded MAC addresses and compare them to the saved ones to identify duplications. Print a message that notifies when a duplication is identified.
5 In the ARP extracting function, pass the filtered data to the current function."""

def check_duplicates(mac_dict):
    seen_mac_list = []
    for ip in mac_dict:
        seen_mac_list.append(mac_dict[ip])
    return seen_mac_list
