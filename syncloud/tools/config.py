from footprint import Footprint

footprints = [
    ('cubieboard', Footprint('sun4i', cpu_count=1)),
    ('cubieboard2', Footprint('sun7i', cpu_count=2, mem_size=847970304)),
    ('cubieboard2', Footprint('sun7i', cpu_count=2, mem_size=1031917568)),
    ('cubietruck', Footprint('sun7i', cpu_count=2, mem_size=1911201792)),
    ('cubietruck', Footprint('sun7i', cpu_count=2, mem_size=2095149056)),
    ('cubietruck', Footprint('sun7i', cpu_count=2, mem_size=2096623616)),
    ('raspberrypi', Footprint('BCM2708')),
    ('beagleboneblack', Footprint('Generic AM33XX (Flattened Device Tree)')),
    ('odroid-xu3', Footprint('ODROID-XU3')),
    ('travis', Footprint(vendor_id='AuthenticAMD'))
]

titles = {
    'cubieboard': 'Cubieboard',
    'cubieboard2': 'Cubieboard2',
    'cubietruck': 'Cubietruck',
    'raspberrypi': 'Raspberry Pi Model B',
    'beagleboneblack': 'BeagleBone Black',
    'odroid-xu3': 'ODROID-XU3',
    'travis': 'Travis'
}