import platform

_system = platform.system()

if (_system in ('Darwin')):
    from darwin import *
elif (_system in ('Linux')):
    from linux import *
elif (_system in ('Windows', 'Microsoft')):
    from windows import *
else:
    raise ImportError("%s is not supported by Aardvark API" % _system)
