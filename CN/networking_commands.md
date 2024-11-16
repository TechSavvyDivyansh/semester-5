# Networking Commands: Windows vs. Linux

## 1. IP Configuration and Interface Information
- **Windows**:  
  - `ipconfig`: Displays basic IP configuration details such as IP address, subnet mask, and default gateway.  
  - `ipconfig /all`: Provides detailed network configuration, including DNS servers, MAC address, and DHCP settings.  

- **Linux**:  
  - `ifconfig` (deprecated, use `ip addr`): Shows network interfaces and their IP addresses.  
  - `ip addr show`: Displays detailed IP address and interface information.  

**Use Case**: Troubleshooting network issues, checking IP addresses, and verifying network adapter settings.  

---

## 2. MAC Address
- **Windows**:  
  - `getmac`: Displays the MAC address of all active network interfaces.  

- **Linux**:  
  - `ip link show`: Lists all network interfaces along with their MAC addresses.  
  - `ifconfig | grep ether`: Extracts MAC addresses from interface details.  

**Use Case**: Identifying devices on a network, configuring access control, or troubleshooting network hardware issues.  

---

## 3. ARP Table
- **Windows**:  
  - `arp -a`: Shows the ARP (Address Resolution Protocol) table with resolved IP-to-MAC address mappings.  

- **Linux**:  
  - `arp -n`: Displays the ARP table without resolving IP addresses to hostnames.  
  - `ip neighbor show`: Shows neighbor cache entries (similar to ARP table).  

**Use Case**: Diagnosing connectivity problems and resolving duplicate IP issues.  

---

## 4. DNS Lookup
- **Windows**:  
  - `nslookup`: Queries DNS servers for domain name resolution.  
  - `nslookup <domain>`: Finds the IP address of a specific domain.  

- **Linux**:  
  - `nslookup`: Similar functionality to Windows.  
  - `dig <domain>`: Performs advanced DNS queries with detailed output.  

**Use Case**: Resolving domain names, verifying DNS configuration, and diagnosing DNS issues.  

---

## 5. Traceroute
- **Windows**:  
  - `tracert <domain>`: Traces the route packets take to reach a specific destination.  

- **Linux**:  
  - `traceroute <domain>`: Provides hop-by-hop details of packet routes to the destination.  

**Use Case**: Identifying network bottlenecks and tracing network paths.  

---

## 6. Network Statistics
- **Windows**:  
  - `netstat`: Displays active connections, ports, and protocol usage.  
  - `netstat -an`: Lists all active ports and their listening states.  

- **Linux**:  
  - `netstat`: Similar functionality to Windows (requires installation on some systems).  
  - `ss -tuln`: A modern alternative for displaying socket and port statistics.  

**Use Case**: Monitoring active connections, troubleshooting port issues, and identifying unauthorized access.  

---

## 7. Ping
- **Windows**:  
  - `ping <domain or IP>`: Sends ICMP echo requests to test connectivity.  

- **Linux**:  
  - `ping <domain or IP>`: Same as Windows.  

**Use Case**: Checking if a host is reachable and measuring network latency.  

---

## 8. Route Information
- **Windows**:  
  - `route print`: Displays the system's routing table.  

- **Linux**:  
  - `route -n`: Shows routing table without DNS resolution.  
  - `ip route show`: Displays routing table in a modern format.  

**Use Case**: Diagnosing routing issues and verifying network routes.  

---

## 9. Hostname
- **Windows**:  
  - `hostname`: Displays the name of the local system.  

- **Linux**:  
  - `hostname`: Same as Windows.  

**Use Case**: Identifying the name of the system for network communication or troubleshooting.  

---

## 10. Open Ports
- **Windows**:  
  - `netstat -an | find "LISTEN"`: Shows all open and listening ports.  

- **Linux**:  
  - `netstat -an | grep LISTEN`: Similar to Windows.  
  - `ss -tuln`: Modern and faster alternative to list open ports.  

**Use Case**: Detecting services running on the system and diagnosing security issues.  

---

## 11. Default Gateway
- **Windows**:  
  - `ipconfig | findstr "Gateway"`: Displays the default gateway.  

- **Linux**:  
  - `ip route | grep default`: Shows the default gateway.  

**Use Case**: Verifying gateway configuration and troubleshooting internet access.  

---

## 12. Test Specific Port Connectivity
- **Windows**:  
  - `telnet <IP> <port>`: Tests connectivity to a specific port on a server.  

- **Linux**:  
  - `telnet <IP> <port>`: Same as Windows.  
  - `nc -zv <IP> <port>`: Modern alternative to test port connectivity.  

**Use Case**: Verifying if a port is open and accessible.  

---

## 13. Check Current User's Connections
- **Windows**:  
  - `net session`: Lists all active sessions.  
  - `net user`: Displays user accounts on the system.  

- **Linux**:  
  - `who`: Lists logged-in users.  
  - `w`: Shows who is logged in and their activities.  

**Use Case**: Monitoring active sessions and user activities.  

---

## 14. Download Files via Command
- **Windows**:  
  - `curl <URL>`: Downloads files or data from a URL.  

- **Linux**:  
  - `curl <URL>`: Similar to Windows.  
  - `wget <URL>`: Another option for downloading files.  

**Use Case**: Downloading files from the internet or APIs.  

---

## 15. Network Performance
- **Windows**:  
  - `iperf3`: A third-party tool for testing network bandwidth.  

- **Linux**:  
  - `iperf3`: Same as Windows.  

**Use Case**: Measuring network performance and diagnosing bandwidth issues.  
