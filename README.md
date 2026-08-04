# Port Scanner

A multithreaded port scanner built in Python from scratch.

## What it does
- Takes target IP as input
- Scans ports 20 to 500 simultaneously using threading
- Identifies open ports and their service names

## How to run
python scanner.py
Enter target IP when prompted

## Example output
22 ssh port is open
80 http port is open
443 HTTPS port is open

## What I learned
- How TCP connections work
- Client side socket programming
- Multithreading in Python
- Class based threading using Thread
- Common port and service mappings

## Tech used
Python, Socket, Threading

## Legal
Only scan IPs you own or have permission to scan.
Never scan without authorization.
