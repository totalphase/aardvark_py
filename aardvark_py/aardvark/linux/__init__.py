import platform

_architecture = platform.architecture()[0]

if (_architecture == '32bit'):
    from arch32 import *
elif (_architecture == '64bit'):
    from arch64 import *
else:
    raise ImportError("%s architecture is not supported by Aardvark API" % _architecture)
