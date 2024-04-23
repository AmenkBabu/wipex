#!/usr/bin/env python3

import argparse
from wipex.interfaces.cli import CLI

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WiPEx - Wireless Access Point Vulnerability Scanner")
    parser.add_argument("-t", "--target", help="Target IP address or network range")
    args = parser.parse_args()

    cli = CLI()
    cli.run(args.target)
