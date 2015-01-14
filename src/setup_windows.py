"""Creates a simple executable for the program using py2exe.
   Windows only!"""

from distutils.core import setup
import py2exe
import sys


if sys.platform == 'win32':
    py2exe_options = dict(excludes=['_ssl', 'pyreadline', 'difflib',
                                    'doctest', 'locale', 'optparse',
                                    'pickle', 'calendar'])
    setup(windows=['main.py'])
else:
    print("The OS detected isn't Windows!")
