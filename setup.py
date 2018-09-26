from setuptools import setup, find_packages

setup(name='ninfo-plugin-geoip',
    version='0.0.3',
    zip_safe=False,
    packages = find_packages(exclude=["tests"]),
    include_package_data=True,
    install_requires=[
        "ninfo>=0.1.11",
        "maxminddb==1.4.1",
    ],
    entry_points = {
        'ninfo.plugin': [
            'geoip = ninfo_plugin_geoip',
        ]
    }
)
