# wipex/modules/discovery/wireless_scanner.py
import subprocess

class WirelessScanner:
    def __init__(self, interface):
        self.interface = interface

    def scan_wireless_networks(self):
        """
        Scan for wireless networks using the specified interface.
        """
        wireless_networks = []
        try:
            # Run the iwlist command to scan for wireless networks
            cmd = f"iwlist {self.interface} scan"
            output = subprocess.check_output(cmd, shell=True, universal_newlines=True)

            # Parse the output to extract wireless network information
            current_network = {}
            for line in output.splitlines():
                if line.strip() == "":
                    if current_network:
                        wireless_networks.append(current_network)
                        current_network = {}
                elif "ESSID" in line:
                    essid = line.split('"')[1]
                    current_network["essid"] = essid
                elif "Encryption key" in line:
                    encryption = line.split(":")[1].strip()
                    current_network["encryption"] = encryption
                elif "Channel" in line:
                    channel = line.split(":")[1].strip()
                    current_network["channel"] = channel
                elif "Frequency" in line:
                    frequency = line.split(":")[1].strip()
                    current_network["frequency"] = frequency
                elif "Signal level" in line:
                    signal_level = line.split("=")[1].strip()
                    current_network["signal_level"] = signal_level

            if current_network:
                wireless_networks.append(current_network)

        except subprocess.CalledProcessError as e:
            print(f"Error scanning wireless networks: {e}")

        return wireless_networks
