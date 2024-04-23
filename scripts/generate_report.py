#!/usr/bin/env python3

import argparse
from wipex.core.reporting import ReportGenerator

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="WiPEx Report Generator")
    parser.add_argument("-i", "--input", required=True, help="Input file containing scan results")
    parser.add_argument("-o", "--output", required=True, help="Output file for the generated report")
    args = parser.parse_args()

    report_generator = ReportGenerator()
    report_generator.generate_report(args.input, args.output)
