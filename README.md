# NetSentinel: The Cyber Vanguard
"Your Digital Watchdog: Unveiling Hidden Threats, Securing Cyberspace"

## Project Description:
NetSentinel is an advanced cybersecurity tool designed to fortify digital defenses by meticulously scanning and identifying potential vulnerabilities and threats in network domains. This Python-based tool harnesses the power of AI and sophisticated network scanning techniques to offer a dual-layered security approach.

## Core Features:

#### 1. Subdomain Enumeration:

  - Utilizes a custom wordlist to systematically uncover and list active subdomains of a given target domain.
  - Employs HTTP requests to validate the existence of each subdomain, filtering out inactive or invalid ones.
  - Integrates a progress bar for real-time tracking of the enumeration process.

#### 2. Port Scanning with Nmap:

  - Conducts a thorough port scan of a specified target IP address using Nmap, a renowned network exploration tool.
  - Detects open ports and services running on these ports, offering insights into potential entry points for cyber threats.

#### 3. Concurrent Execution:

  - Implements concurrent futures for simultaneous subdomain enumeration and Nmap scanning, optimizing the time and efficiency of the security analysis.

#### 4. Result Compilation and Reporting:

  - Aggregates and logs the results of both subdomain enumeration and Nmap scans into a comprehensive output file.
  - Provides a detailed view of the scanned network landscape, aiding in further cybersecurity analysis and decision-making.

## Requirements to run the script successfully
To effectively use and run NetSentinel, ensure the following prerequisites are met:

#### Python Environment:
  - Python 3.x installed.
  - Preferred IDE or text editor for Python development.
#### Libraries and Dependencies:
  - **requests**: For making HTTP requests during subdomain enumeration.
  - **nmap**: Python library for interacting with the Nmap port scanner.
  - **concurrent.futures**: For efficient concurrent execution.
  - **tqdm**: For real-time progress visualization during scanning processes.

#### Nmap Installation:
  - Nmap must be installed on your system as the nmap Python library acts as a wrapper for the Nmap tool.

## Running the Code
After ensuring all the requirements are met, run the NetSentinel tool as follows:

  - Open your Python environment or terminal.
  - Navigate to the directory containing the NetSentinel project files.
  - Execute the main script by running the command: python main.py.
  - Follow the on-screen prompts to input the target domain, wordlist file path, and target IP for Nmap scanning.

## Technical Stack:

  - **Language**: Python
  - **Key Libraries**: requests for HTTP operations, nmap for port scanning, 'concurrent.futures' for parallel task execution, and tqdm for progress visualization.

## Usage Scenario:
NetSentinel is an invaluable asset for cybersecurity professionals, network administrators, and digital security enthusiasts. It serves as a proactive tool in identifying potential vulnerabilities in network infrastructures, allowing for preemptive security enhancements. Whether it's securing corporate networks or safeguarding personal digital domains, NetSentinel stands as a vigilant protector in the ever-evolving cyber landscape.
