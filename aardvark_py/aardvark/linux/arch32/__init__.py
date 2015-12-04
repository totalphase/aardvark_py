try:
    from aardvark import *
except ImportError:
    import imp
    imp.load_dynamic('aardvark', 'aardvark.so')
    from aardvark import *
