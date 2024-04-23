import android.net.wifi.WifiManager
from android.content import Context

class MobileHotspotScanner:
    def __init__(self, context: Context):
        self.wifi_manager = context.getSystemService(Context.WIFI_SERVICE)

    def scan_mobile_hotspot(self):
        try:
            hotspot_state = self.wifi_manager.isWifiApEnabled()
            if hotspot_state:
                hotspot_config = self.wifi_manager.getWifiApConfiguration()
                return {
                    "ssid": hotspot_config.SSID,
                    "encryption": hotspot_config.getAuthType()
                }
            else:
                return None
        except Exception as e:
            print(f"Error scanning mobile hotspot: {e}")
            return None
