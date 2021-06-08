# Camelot
Assistive Transport Robot

This branch is a collection of ROS2 packages containing the source code for Camelot.

## Raspberry Pi Setup

### Initial setup
- Flash Ubuntu Server 20.04 on to the SD card
- Connect via Ethernet to router in `Hotspot Router` mode
- `sudo apt update && sudo apt upgrade`

### Installing ROS2
- Use these instructions: https://docs.ros.org/en/foxy/Installation/Ubuntu-Install-Debians.html

### Setting up I2C for the OLED
- Connect OLED to I2C pins
- `sudo apt install i2c-tools python3-pip`
- Following this guide: https://learn.adafruit.com/monochrome-oled-breakouts/python-setup
- `sudo pip3 install --upgrade setuptools`
- `sudo pip3 install adafruit-blinka`
- `sudo pip3 install adafruit-circuitpython-ssd1306`
- Run the OLED program with `sudo python3 oled.py`
- To run on startup add `@reboot /home/ubuntu/oled.py` to the root crontab

### Connecting to motor controller via UART
- Helpful link: https://www.raspberrypi.org/documentation/configuration/uart.md
- Stackoverflow instructions for enabling UART on Ubuntu for Raspberry Pi: https://askubuntu.com/questions/1254376/enable-uart-communication-on-pi4-ubuntu-20-04
