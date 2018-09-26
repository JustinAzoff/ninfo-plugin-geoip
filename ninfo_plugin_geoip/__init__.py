from ninfo import PluginBase
import maxminddb

class geoip_plug(PluginBase):
    """This plugin returns geographic information on an IP"""
    name    =    'geoip'
    title   =    'GeoIP'
    description   =  'Geographic IP location'
    types   =    ['ip', 'ip6']
    local = False

    def setup(self):
        path  = self.plugin_config['path']
        self.g = maxminddb.open_database(path)

    def get_info(self, ip):
        record = self.g.get(ip)
        if record:
            record.setdefault('country', None)
            record.setdefault('autonomous_system_number', None)
        return record

plugin_class = geoip_plug
