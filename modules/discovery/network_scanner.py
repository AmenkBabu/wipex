# wipex/modules/discovery/network_scanner.py
import subprocess
import nmap

class NetworkScanner:
    def __init__(self, network_range):
        self.network_range = network_range
        self.nm = nmap.PortScanner()

    def scan_network(self, scan_type="tcp_connect", ports=None):
        """
        Scan the specified network range using the specified scan type and ports.
        """
        devices = []
        try:
            # Prepare the arguments for the nmap scan
            arguments = "-sn"  # Default to ping scan
            if scan_type == "tcp_connect":
                arguments = "-sT"  # TCP connect scan
            elif scan_type == "syn":
                arguments = "-sS"  # SYN scan
            if ports:
                arguments += f" -p{ports}"

            # Run the nmap scan on the specified network range
            self.nm.scan(hosts=self.network_range, arguments=arguments)

            # Iterate over the identified hosts
            for host in self.nm.all_hosts():
                device_info = self.nm[host]
                devices.append({
                    'ip': host,
                    'mac': device_info['addresses'].get('mac', 'Unknown'),
                    'vendor': self._get_vendor(device_info),
                    'ports': self._get_open_ports(device_info),
                })

        except Exception as e:
            print(f"Error scanning network: {e}")

        return devices

    def _get_vendor(self, device_info):
        # Lookup the vendor based on the MAC address
        mac_address = device_info['addresses'].get('mac', '')
        if mac_address:
            # Use a library or API to lookup the vendor based on the MAC address
            # Example: https://macvendors.com/
            pass
        return 'Unknown'

    def _get_open_ports(self, device_info):
        open_ports = []
        for port in device_info['tcp'].keys():
            if device_info['tcp'][port]['state'] == 'open':
                open_ports.append(port)
        return open_ports
