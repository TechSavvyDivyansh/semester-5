def get_class_details(ip):
    
    first_byte=int(ip.split(".")[0])
    if 0<=first_byte<=127:
        ip_class='A'
        subnet_mask='255.0.0.0'
    elif 128<=first_byte<=191:
        ip_class='B'
        subnet_mask='255.255.0.0'
    elif 192<=first_byte<=223:
        ip_class='C'
        subnet_mask='255.255.255.0'
    elif 224<=first_byte<=239:      
        ip_class='D'
        subnet_mask='none'
        return ip_class, subnet_mask, 'N/A', 'N/A'
    elif 240<=first_byte<=255:
        ip_class='E'
        subnet_mask='none'
        return ip_class, subnet_mask, 'N/A', 'N/A'


    first_ip=and_operation(ip,subnet_mask)
    last_ip=notor_operation(ip,subnet_mask)
    
    return ip_class,subnet_mask,first_ip,last_ip


def and_operation(ip,subnet):
    # Convert IP address and subnet mask to binary
    ip_octets = [int(octet) for octet in ip.split('.')]
    mask_octets = [int(octet) for octet in subnet.split('.')]

    # Perform the bitwise AND operation
    network_octets = [ip_octet & mask_octet for ip_octet, mask_octet in zip(ip_octets, mask_octets)]

    # Convert the result back to a string in dotted-decimal format
    network_address = ".".join(map(str, network_octets))
    return network_address


def notor_operation(ip,subnet):
    # Convert IP address and subnet mask to binary
    ip_octets = [int(octet) for octet in ip.split('.')]
    mask_octets = [~int(octet) & 0xFF for octet in subnet.split('.')]

    # Perform the bitwise AND operation
    network_octets = [ip_octet | mask_octet for ip_octet, mask_octet in zip(ip_octets, mask_octets)]

    # Convert the result back to a string in dotted-decimal format
    network_address = ".".join(map(str, network_octets))
    return network_address



ip=input("Enter you ip:")
ip_split=ip.split(".")
print("\n")

if len(ip_split)>4 or all(int(octet)>255 for octet in ip_split):
    print("invalid ip address")
else:
    ip_class,subnet_mask,first_ip,last_ip=get_class_details(ip)
    print(f"class:{ip_class},\nsubnet mask:{subnet_mask},\nfirst_ip:{first_ip},\nlast_ip:{last_ip}\n")