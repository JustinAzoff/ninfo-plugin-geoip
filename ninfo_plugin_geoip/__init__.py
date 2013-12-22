from ninfo import PluginBase
import pygeoip

record_keys = ['city', 'region_name', 'region', 'area_code', 'time_zone', 'longitude', 'metro_code', 'country_code3', 'latitude', 'postal_code', 'dma_code', 'country_code', 'country_name']

class geoip_plug(PluginBase):
    """This plugin returns geographic information on an IP"""
    name    =    'geoip'
    title   =    'GeoIP'
    description   =  'Geographic IP location'
    types   =    ['ip']
    local = False

    def setup(self):
        path  = self.plugin_config['path']
        self.g = pygeoip.GeoIP(path)

    def get_info(self, ip):
        try :
            record = self.g.record_by_addr(ip)
        except pygeoip.GeoIPError:
            record = dict.fromkeys(record_keys, None)
            record['country_code'] = self.g.country_code_by_addr(ip)
            record['country_name'] = self.g.country_name_by_addr(ip)
        return record

plugin_class = geoip_plug
