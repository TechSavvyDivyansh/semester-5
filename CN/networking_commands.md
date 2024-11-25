`note : for exam refer only commands for windows till 8.Route Information`

# Networking Commands: Windows vs. Linux

## 1. IP Configuration and Interface Information
- **Windows**:  
  - `ipconfig`: View IP configuration.  
  - `ipconfig /all`: Detailed network settings.  

- **Linux**:  
  - `ip addr` : Show network details.  

**Use Case**: Check IP, subnet, and adapter info.  

---

## 2. MAC Address
- **Windows**:  
  - `getmac`: Display MAC addresses.  

- **Linux**:  
  - `ip link show`: Show MAC of interfaces.  
  - `ip addr | grep ether`: Extract MAC address.  

**Use Case**: Identify devices or manage access.  

---

## 3. ARP Table
- **Windows**:  
  - `arp -a`: View IP-to-MAC mappings.  

- **Linux**:  
  - `arp -n`: Display ARP table.  
  - `ip neighbor show`: Show neighbor cache.  

**Use Case**: Debug connectivity or IP conflicts.  

---

## 4. DNS Lookup
- **Windows**:  
  - `nslookup`: Query DNS for domain info.  

- **Linux**:  
  - `nslookup`: Same as Windows.  
  - `dig`: Advanced DNS queries.  

**Use Case**: Resolve domain names.  

---

## 5. Traceroute
- **Windows**:  
  - `tracert`: Trace the path to a destination.  

- **Linux**:  
  - `traceroute`: Same as Windows.  

**Use Case**: Identify network delays.  

---

## 6. Network Statistics
- **Windows**:  
  - `netstat`: Show active connections.  

- **Linux**:  
  - `netstat`: Same as Windows.  
  - `ss -tuln`: Modern alternative for socket info.  

**Use Case**: Monitor connections and ports.  

---

## 7. Ping
- **Windows**:  
  - `ping`: Test connectivity to a host.  

- **Linux**:  
  - `ping`: Same as Windows.  

**Use Case**: Check host availability.  

---

## 8. Route Information
- **Windows**:  
  - `route print`: Display routing table.  

- **Linux**:  
  - `route -n`: Show routes.  
  - `ip route show`: Modern routing table display.  

**Use Case**: Diagnose routing issues.  

---

## 9. Hostname
- **Windows**:  
  - `hostname`: Get the system name.  

- **Linux**:  
  - `hostname`: Same as Windows.  

**Use Case**: Identify system on a network.  

---

## 10. Open Ports
- **Windows**:  
  - `netstat -an | find "LISTEN"`: Show listening ports.  

- **Linux**:  
  - `netstat -an | grep LISTEN`: Same as Windows.  
  - `ss -tuln`: Modern open port viewer.  

**Use Case**: Check running services or security.  

---

## 11. Default Gateway
- **Windows**:  
  - `ipconfig | findstr "Gateway"`: View default gateway.  

- **Linux**:  
  - `ip route | grep default`: Show default gateway.  

**Use Case**: Verify internet gateway.  

---

## 12. Test Specific Port Connectivity
- **Windows**:  
  - `telnet`: Test server port connectivity.  

- **Linux**:  
  - `telnet`: Same as Windows.  
  - `nc -zv`: Modern connectivity tester.  

**Use Case**: Test if ports are open.  

---

## 13. Check Current User's Connections
- **Windows**:  
  - `net session`: List active sessions.  
  - `net user`: Show user accounts.  

- **Linux**:  
  - `who`: View logged-in users.  
  - `w`: Show user activity.  

**Use Case**: Monitor sessions or users.  

---

## 14. Download Files via Command
- **Windows**:  
  - `curl`: Fetch files from a URL.  

- **Linux**:  
  - `curl`: Same as Windows.  
  - `wget`: Another file downloader.  

**Use Case**: Download files or data.  
