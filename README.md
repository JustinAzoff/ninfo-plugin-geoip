ninfo-plugin-geoip
==================

GeoIP plugin for ninfo, see https://github.com/JustinAzoff/ninfo

Configuration
-------------

```
[plugin:geoip]
path = /path/to/geolite
```

For the city database:

```
[plugin:geoipcity]
clone = geoip
title = City GeoIP
description = City Level GeoIP
path = /path/to/geolitecity
```

You can get the databases from Maxmind's site here:
http://dev.maxmind.com/geoip/legacy/geolite/

Note that the plugin currently only supports the legacy GeoLite country
database, not the GeoLite2 databases.

