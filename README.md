# Python Network Monitoring Tool

This network monitoring tool is developed using Python and the `python-nmap` library. It provides a simple command-line interface to perform network scans for open ports on a specified target host.

## Features

- Scan a specified target host for open ports within a specified port range.
- Display the scan results, including the state of each port for each protocol.

## Prerequisites

- Python 3.6 or higher
- Nmap (https://nmap.org/download.html)
- python-nmap library (https://github.com/savon-noir/python-nmap)

## Installation

1. Install Nmap on your system. Download it from https://nmap.org/download.html and follow the installation instructions for your platform.

2. Install the `python-nmap` library using pip:
``` py -m pip install python-nmap ```

3. Clone this repository to your local machine:
``` git clone https://github.com/tdolan21/nmap-portscanner.git ```


## Usage

1. Navigate to the project directory:


2. Run the Python script:

``` python nmap-portscanner.py ```

3. The script will prompt you for the target host and port range. Enter the desired values and the scan will begin.

4. Once the scan is complete, the results will be displayed in the terminal.

## Disclaimer

Always ensure you have permission from the target host owner before performing a scan. Scanning a host without permission can be considered malicious activity. The example provided in the script uses 'scanme.nmap.org', which is specifically set up by the Nmap team for testing purposes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
