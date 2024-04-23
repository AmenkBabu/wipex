import unittest
from unittest.mock import patch
from wipex.core.fingerprinter import Fingerprinter

class TestFingerprinter(unittest.TestCase):
    @patch('wipex.core.fingerprinter.Fingerprinter.fingerprint_device')
    def test_fingerprint_device(self, mock_fingerprint_device):
        fingerprinter = Fingerprinter()
        device_info = {'mac': '00:11:22:33:44:55', 'model': 'Linksys WRT54G'}
        fingerprinter.fingerprint_device(device_info)
        mock_fingerprint_device.assert_called_once_with(device_info)

if __name__ == '__main__':
    unittest.main()
