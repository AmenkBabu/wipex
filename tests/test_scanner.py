import unittest
from unittest.mock import patch
from wipex.core.scanner import Scanner

class TestScanner(unittest.TestCase):
    @patch('wipex.core.scanner.Scanner.scan_network')
    def test_scan_network(self, mock_scan_network):
        scanner = Scanner()
        scanner.scan_network('192.168.1.0/24')
        mock_scan_network.assert_called_once_with('192.168.1.0/24')

if __name__ == '__main__':
    unittest.main()
