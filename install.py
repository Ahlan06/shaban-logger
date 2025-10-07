#!/usr/bin/env python3
"""
Automatic installation script for Shaban Logger
"""

import sys
import subprocess
import importlib
import os

def check_python_version():
    """Check Python version"""
    if sys.version_info < (3, 8):
        print("Python 3.8 or higher is required")
        sys.exit(1)
    print(f"Python {sys.version_info.major}.{sys.version_info.minor} detected")

def install_dependencies():
    """Install missing dependencies"""
    dependencies = [
        "requests",
        "pillow", 
        "psutil",
        "pyautogui",
        "colorama"
    ]
    
    print("Installing dependencies...")
    
    for package in dependencies:
        try:
            importlib.import_module(package)
            print(f"{package} already installed")
        except ImportError:
            print(f"Installing {package}...")
            try:
                subprocess.check_call([
                    sys.executable, "-m", "pip", "install", package
                ])
                print(f"{package} successfully installed")
            except subprocess.CalledProcessError:
                print(f"Installation failed for {package}")
                return False
    return True

def main():
    print("Shaban Logger - Installation")
    print("=" * 40)
    
    check_python_version()
    
    if install_dependencies():
        print("\nInstallation completed successfully!")
        print("You can now run: python combined_logger.py")
    else:
        print("\nInstallation failed")
        sys.exit(1)

if __name__ == "__main__":
    main()