# Relative imports: https://docs.python.org/2.5/whatsnew/pep-328.html
# make constants submodule visible to pkg module
from . import constants
# make things from internal_script.py visible
from .internal_script import *
