import socket
from threading import Thread

ip = (input("enter ip: "))

class Port_Scanner(Thread):
    def __init__(self, ip, port):
        super().__init__()
        self.port = port
        self.ip = ip
        self.s = socket.socket()

    def run(self):
        self.s.settimeout(20)

        addr = (self.ip, self.port)
        result = self.s.connect_ex(addr)

        if result == 0:
            print(f"{self.port} {known_ports.get(self.port, 'Unknown Service')} port is open")
            return(self.port, self.grab_banner())

    def grab_banner(self):
        try:
            data = self.s.recv(1024)
            banner= data.decode('utf-8')
            print(f"Banner → {banner}")
            return banner
        except TimeoutError:
            print("timeout error")
        except Exception:
            print("could not read banner")

known_ports = {
    1: "tcpmux",  # TCP Port Service Multiplexer
    7: "echo",  # Echo Protocol
    5: "rje",  # Remote Job Entry
    9: "discard",  # Discard Protocol
    11: "systat",  # Active Users
    13: "daytime",  # Daytime Protocol
    17: "qotd",  # Quote of the Day
    18: "msp",  # Message Send Protocol
    19: "chargen",  # Character Generator Protocol
    20: "ftp-data",  # File Transfer Protocol (data)
    21: "ftp",  # File Transfer Protocol (control)
    22: "ssh",  # Secure Shell
    23: "telnet",  # Telnet Protocol
    25: "smtp",  # Simple Mail Transfer Protocol
    37: "time",  # Time Protocol
    42: "nameserver",  # WINS Host Name Server
    43: "nicname",  # WHOIS Protocol
    49: "tacacs",  # TACACS Login Protocol
    53: "domain",  # Domain Name System (DNS)
    67: "bootps",  # Bootstrap Protocol (DHCP server)
    68: "bootpc",  # Bootstrap Protocol (DHCP client)
    69: "tftp",  # Trivial File Transfer Protocol
    79: "finger",  # Finger Protocol
    80: "http",  # World Wide Web HTTP
    88: "kerberos",  # Kerberos Securitty
    101: "hostname",  # NIC Host Name Server
    443: "HTTPS"
}

for port in range(20,82):
    scanner = Port_Scanner(ip, port)
    scanner.start()
