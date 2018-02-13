import platform

_system = platform.system()
_architecture = platform.architecture()[0]
_supported_systems = ('Linux')

if (_system in _supported_systems):
    if (_architecture == '32bit'):
        from .arch32 import *
    elif (_architecture == '64bit'):
        from .arch64 import *
    else:
        raise ImportError("Unable to import %s Aardvark API extension module on %s architecture" % ( _supported_systems, _architecture))
else:
    raise ImportError("Unable to import %s Aardvark API extension module on %s system" % ( _supported_systems, _system))
