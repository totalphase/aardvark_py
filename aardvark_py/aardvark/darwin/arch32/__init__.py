import platform

_system = platform.system()
_architecture = platform.architecture()[0]

if ((_system in ('Darwin')) and (_architecture == '32bit')):
    from .aardvark import *
