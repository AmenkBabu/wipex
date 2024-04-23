import argparse
from wipex.core.scanner import Scanner
from wipex.core.fingerprinter import Fingerprinter
from wipex.core.vulnerability_scanner import VulnerabilityScanner
from wipex.modules.discovery.network_scanner import NetworkScanner
from wipex.modules.discovery.wireless_scanner import WirelessScanner
from wipex.modules.identification.device_identifier import DeviceIdentifier
from wipex.modules.vulnerability.vulnerability_scanner import VulnerabilityScanner
from wipex.modules.wireless.encryption import EncryptionAnalyzer
from wipex.modules.wireless.firmware import FirmwareAnalyzer
from wipex.modules.wireless.default_creds import DefaultCredentialsChecker
def main():
    parser = argparse.ArgumentParser(description='WiPEx - Wireless Penetration Tester')
    parser.add_argument('-i', '--interface', required=True, help='Wireless interface to use')
    args = parser.parse_args()

    # Scan for networks and devices
    network_scanner = NetworkScanner(args.interface)
    wireless_scanner = WirelessScanner(args.interface)
    networks = network_scanner.scan_networks()
    devices = wireless_scanner.scan_wireless_devices()

    # Fingerprint devices
    for device in devices:
        device_identifier = DeviceIdentifier(device)
        device_identifier.identify_device()

    # Scan for vulnerabilities
    for device in devices:
        vulnerability_scanner = VulnerabilityScanner(device)
        vulnerability_scanner.scan_for_vulnerabilities()

    # Analyze wireless security aspects
    for network in networks:
        encryption_analyzer = EncryptionAnalyzer(network)
        encryption_analyzer.analyze_encryption()

    for device in devices:
        firmware_analyzer = FirmwareAnalyzer(device)
        firmware_analyzer.analyze_firmware()

        default_creds_checker = DefaultCredentialsChecker(device)
        default_creds_checker.check_default_credentials()

    # Print results
    print("Wireless Network Summary:")
    for network in networks:
        print(f"SSID: {network.ssid}, Encryption: {network.encryption}")

    print("\nDevice Summary:")
    for device in devices:
        print(f"Device: {device.name}, Vendor: {device.vendor}, Vulnerabilities: {', '.join(device.vulnerabilities)}")

if __name__ == '__main__':
    main()
