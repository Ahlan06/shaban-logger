<p align="center">
  
</p>

<p align="center">
Advanced System Monitoring and Logging Tool
</p>

<p align="center">
  <img width="1338" height="429" alt="image" src="https://github.com/user-attachments/assets/e580c13c-2ff6-41ed-994f-76ca62fc8b83" />
<a href="https://github.com/Ahlan06/shaban-logger/commits/main"><img src="https://img.shields.io/badge/version-1.0.0-blue"></a>
<a href="https://github.com/Ahlan06/shaban-logger/blob/main/README.md"><img src="https://img.shields.io/badge/docs-passing-brightgreen.svg"></a>
<a href="https://github.com/Ahlan06/shaban-logger/blob/main/LICENSE"><img src="https://img.shields.io/github/license/Ahlan06/shaban-logger.svg"></a>
<a href="https://github.com/Ahlan06/shaban-logger/graphs/contributors"><img src="https://img.shields.io/github/contributors/Ahlan06/shaban-logger.svg"></a>
<a href="https://github.com/Ahlan06/shaban-logger/network/members"><img src="https://img.shields.io/github/forks/Ahlan06/shaban-logger.svg"></a>
</p>

## About Shaban Logger

**Shaban Logger** is an advanced system monitoring and logging tool designed for security professionals and system administrators. It provides comprehensive system information collection, screenshot capture, network monitoring, and process logging capabilities.

*In tribute to Shaban, a young computer engineering graduate in Gaza, whose memory reflects the strength, knowledge, and hope of a people seeking justice.*

### Features

- **System Information** - Collect detailed system specs and configuration
- **Network Monitoring** - Network interface and connection tracking
- **Process Logging** - Real-time process monitoring
- **Cross-Platform** - Works on Windows and Linux systems

---

## Installation

### Prerequisites

### Python 3.8 or higher

**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- Install with "Add Python to PATH" checked

**Linux/MacOS:**
```bash
# Check if installed
python3 --version

# If not installed:
sudo apt install python3 python3-pip    # Linux
brew install python3                    # MacOS
bash
```
### Git

### Download for Windows 

Download with `git`:

```bash
# Clone the repository
git clone https://github.com/Ahlan06/shaban-logger.git
cd shaban-logger

# Install dependencies
pip install requests pillow psutil pyautogui colorama

# Run the application
python shaban.py

```bash
git clone https://github.com/Ahlan06/shaban-logger.git

# Clone the repository
git clone https://github.com/Ahlan06/shaban-logger.git
cd shaban-logger

# Remove any existing virtual environment (if present)
rm -rf venv

# Run the automatic installer
python3 install.py

# Start the application
./run_shaban.sh
bash
 ```

```
## Webhook Configuration

### What is a Webhook?

A webhook is a way for applications to provide real-time information to other applications. In Shaban Logger, it's used to send collected data to your specified endpoint.

### How to Get a Webhook

#### Discord Webhook (Recommended)

1. **Create a Discord Server** or use an existing one
2. **Go to Server Settings** → **Integrations** → **Webhooks**
3. **Click "New Webhook"**
4. **Name it** (e.g., "Shaban Logger")
5. **Copy the Webhook URL**
6. **Use this URL in your configuration**

 ## 📊 **Shaban Logger - System Monitoring Demo**
<img width="1094" height="989" alt="image" src="https://github.com/user-attachments/assets/ff25dcf8-08de-4c68-a9dc-0801b2083c10" />

## Complete System Intelligence Gathering

This screenshot demonstrates Shaban Logger's powerful monitoring capabilities, showing comprehensive system data collection including:

### 🔍 **Data Collected:**
- **🌐 Network Info**: Public IP, ISP, Geolocation (Minsk, Belarus)
- **💻 System Specs**: Linux OS, GB RAM,GB disk, architecture  
- **👤 User Data**: Root user, hostname, system time tracking
- **🛠️ Technical Details**: Python 3.13.7, MAC address, local IP

### 🎯 **Key Features Shown:**
- Real-time system monitoring
- Geolocation mapping
- Hardware inventory
- Network configuration analysis
- Multi-layer data correlation

**Perfect for security audits and system administration** - providing complete visibility into system operations and network footprint.

# Project Structure

shaban-logger/
├── install.py           # Automatic dependency installer
├── combined_logger.py   # Main logging system
├── shaban.py           # Additional monitoring tools
├── run_shaban.sh       # Linux/Mac launcher script
├── run_shaban.bat      # Windows launcher script
└── README.md           # Documentation

# Dependencies
requests - HTTP library for network operations

pillow - Image processing for screenshot capture

psutil - System utilities for process monitoring

pyautogui - Screenshot capture functionality

colorama - Terminal colors for better output

# Supported Systems
Windows 10/11

Linux (Kali Linux, Ubuntu, Debian)

macOS (Untested but should work)

# In Memoriam of Shaban Al Dalu
This project is named after Shaban, a young Palestinian computer scientist from Gaza who had his whole life ahead of him. He died at the age of 19 during the bombing of Al-Aqsa Hospital by the Israeli Defense Forces on October 14, 2024.
This tool aims to provide clarity and visibility, principles embodied in Shaban's memory.

# Legal Disclaimer
### Intended Use
This tool is intended for:

Educational purposes

Security research

System administration

Authorized penetration testing

Personal systems you own

# Prohibited Use
### STRICTLY PROHIBITED:

Unauthorized system monitoring

Illegal surveillance

Malicious activities

Any use without proper authorization

# Responsibility
I'm not responsible for misuse of this software. Users are solely responsible for ensuring they have proper authorization before using this tool on any system.

# Security Note
### This tool is designed for:

Security professionals

IT administrators

Researchers

Authorized testing environments

Always ensure you have proper authorization before using on any system.

# Support
### For issues and questions:

Check the troubleshooting section above

Ensure all dependencies are installed

Verify Python version compatibility

Check the GitHub Issues page

# Author
Ahlan Mira - Student Security Researcher

# License
This project is provided for educational and research purposes.

<div align="center">
IN MEMORY OF SHABAN

May this tool ensure that his name is never forgotten.

USE RESPONSIBLY 

Only use on systems you own or have explicit permission to test.

</div> 



