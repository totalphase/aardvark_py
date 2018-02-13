import platform

_system = platform.system()
_architecture = platform.architecture()[0]
_supported_systems = ('Windows', 'Microsoft')
_supported_architecture = '64bit'

if ((_system in _supported_systems) and (_architecture == _supported_architecture)):
    from .aardvark import *
else:
    raise ImportError("Unable to import %s %s Aardvark API extension module on %s %s system" % ( _supported_systems, _supported_architecture, _system, _architecture))
