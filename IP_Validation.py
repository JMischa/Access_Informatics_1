#!/usr/bin/env python3

def is_valid_IPv4_octet(octet):
    """Returns True if octet represents a valid IPv4 octet, False otherwise"""
    if octet.isnumeric() == True:
        if int(octet) in range(0,256):
            return True
        else:
            return False
    else:
        return False

def is_valid_IPv4(ip):
    """Returns True if ip represents a valid IPv4 address, False otherwise"""
    section = ip.split('.')
    ans = []
    for octet in section:
        ans.append(is_valid_IPv4_octet(octet))
    lenght_ans = 0
    for i in ans:
        lenght_ans += 1

    if False in ans or lenght_ans < 4:
        return False
    else:
        return True

def is_valid_IPv6_hextet(hextet):
    """Returns True if hextet represents a valid IPv6 hextet, False otherwise"""
    res = hextet.lower()
    if len(res) <= 4:
        if res.isnumeric() or all(c in '0123456789abcdef' for c in res):
            res = int(res, 16)
            if 0 <= res <= 65535:
                return True

    return False

def is_valid_IPv6(ip):
    """Returns True if ip represents a valid IPv6 address, False otherwise"""
    if ip == "":
        return False
    hextets = ip.split(':')
    ans = []
    for hextet in hextets:
        ans.append(is_valid_IPv6_hextet(hextet))
    lenght_ans = 0
    for i in ans:
        lenght_ans += 1
    
    if False in ans or lenght_ans != 8:
        return False
    else:
        return True


def is_valid_IP(ip):
    """Returns True if ip represents a valid IPv4 or IPv6 address False otherwise"""
    IPv4_check = is_valid_IPv4(ip)
    IPv6_check = is_valid_IPv6(ip)
    if IPv4_check or IPv6_check == True:
        return True

    else:
        return False
# You should look at task/test.py and extend the test suite we provided!


print(is_valid_IPv6('fe80:8:1:2:2:2:2:2'))