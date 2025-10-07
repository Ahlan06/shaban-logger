<p align="center">
  
</p>

<p align="center">
Advanced System Monitoring and Logging Tool
</p>

<p align="center">
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
- **Screenshot Capture** - Automatic screenshot logging  
- **Network Monitoring** - Network interface and connection tracking
- **Process Logging** - Real-time process monitoring
- **Cross-Platform** - Works on Windows and Linux systems

---

## Installation

### Prerequisites

- **Python 3.8** or higher
- **Git** (recommended for cloning)

### Download for Linux (Kali, Ubuntu, Debian...)

Download with `git`:

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
```
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

# In Memoriam
This project is named after Shaban, a young Palestinian computer scientist from Gaza with his whole life ahead of him, whose story illustrates the ongoing struggle for justice and transparency. This tool aims to bring clarity and visibility—principles embodied in Shaban's memory.

# Legal Disclaimer
Intended Use
This tool is intended for:

Educational purposes

Security research

System administration

Authorized penetration testing

Personal systems you own

# Prohibited Use
STRICTLY PROHIBITED:

Unauthorized system monitoring

Illegal surveillance

Malicious activities

Any use without proper authorization

# Responsibility
The authors are not responsible for misuse of this software. Users are solely responsible for ensuring they have proper authorization before using this tool on any system.

#Security Note
This tool is designed for:

Security professionals

IT administrators

Researchers

Authorized testing environments

Always ensure you have proper authorization before using on any system.

# Support
For issues and questions:

Check the troubleshooting section above

Ensure all dependencies are installed

Verify Python version compatibility

Check the GitHub Issues page

# Author
Ahlan06 - Security Researcher

# License
This project is provided for educational and research purposes.

<div align="center">
IN MEMORY OF SHABAN

May this tool ensure that his name is never forgotten.

USE RESPONSIBLY 

Only use on systems you own or have explicit permission to test.

</div> 



