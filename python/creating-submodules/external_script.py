# pkg comes from directory name with an __init__.py file inside
# constants comes from pkg/constants directory name.
# When you import a package, package/__init__.py runs automatically, so you can put more import statements inside. if necessary.
from module import constants, internal
# from module.constants import * would work too
# also import module.constants.flags as flags; we have tons of options


# Usage from *outside* the package
def external():
    print('=' * 5 + 'external' + '=' * 5)
    print('constants.LED_LEFT: {}'.format(hex(ord(constants.LED_LEFT))))
    print('constants.LED_RIGHT: {}'.format(hex(ord(constants.LED_RIGHT))))
    print('constants.LED_LEFT_PIN: {}'.format(constants.LED_LEFT_PIN))

internal()
external()

print('=' * 15)
# Not really constants, basically global variables
print(constants.NAME)
constants.NAME = 'Larry'
print(constants.NAME)
