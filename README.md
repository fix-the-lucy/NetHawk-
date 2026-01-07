# 🦅 NetHawk
**A Lightweight Network Reconnaissance & IP Discovery Suite**

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Status](https://img.shields.io/badge/status-Educational-orange.svg)]()

NetHawk is a streamlined utility designed for network administrators and security enthusiasts. It combines deep port analysis with rapid IP identification into a single, easy-to-use Python toolset.

---

## 🛑 Critical Precautions & Legal Warning

> **IMPORTANT:** Network scanning without explicit permission is illegal. This tool is intended for **Educational Purposes Only** and authorized security testing.

* **Authorization:** Only scan hardware and networks you own or have written consent to test.
* **Network Stability:** Full-range scans (1-65535) generate significant traffic and can cause latency or crashes on older network equipment.
* **Privacy:** Your public IP is retrieved via external APIs. Be aware that these services may log request metadata.
* **Security Alerts:** Modern firewalls and IDS (Intrusion Detection Systems) will likely flag and block your IP for "Port Sweeping."

---

## 🛠️ Key Features

### 🔍 1. Multi-Port Scanner
Iterates through possible ports on a target host to identify entry points and running services.
* **Timeout Handling:** Includes a 1-second default timeout to prevent hanging on filtered ports.
* **Error Reporting:** Handles hostname resolution and connection failures gracefully.

### 🌐 2. IP Intelligence Suite
A three-tier discovery system to map your network footprint:
* **Local Discovery:** Identify your machine name and internal LAN IP.
* **Global Discovery:** Fetch your external WAN IP via the `ipify` API.
* **Domain Resolution:** Convert any URL (e.g., *google.com*) into its physical IP address.

---

## 🚀 Getting Started

### Prerequisites
* **Python 3.6+**
* No external dependencies required (uses standard libraries `socket`, `json`, and `urllib`).

### Installation
```bash
# Clone the repository
git clone https://github.com/fix-the-lucy/NetHawk

# Navigate to the directory
cd NetHawk-

```
## Usage 

# To scan for open ports
``` bash
python port_scanner.py
```

# To find IP information
```
python ip_finder.py
```

## ⚖️ License

Distributed under the MIT License.
Copyright (c) 2026 fix-the-lucy
Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software.

## 📂 Project Structure

- port_scanner.py: The main engine for scanning target ports.
- ip_finder.py: Utility for local, public, and DNS IP resolution.
- README.md: Documentation and safety guidelines.

## 🛡️ Disclaimer

# The developer assumes no liability and is not responsible for any misuse or damage caused by this program. Use NetHawk ethically to improve your own network security awareness, not to compromise others.

## 🤝 Support & Feedback

# Thank you for using NetHawk! If you find this tool helpful, consider giving it a ⭐ on GitHub.

# Found a bug or have a suggestion? Please feel free to Open an Issue or submit a Pull Request. Your feedback helps make this tool better for everyone.

### Stay Safe & Happy Coding!
