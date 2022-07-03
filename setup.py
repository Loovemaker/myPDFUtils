from setuptools import setup
from sys import argv

assert len(argv) >= 2
platform = argv[1]

if platform == 'py2exe':
    import py2exe
    from setup_options.setup_py2exe import setup_kwargs
elif platform == 'py2app':
    import py2app
    from setup_options.setup_py2app import setup_kwargs
else:
    raise ValueError()

setup(**setup_kwargs)
