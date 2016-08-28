from . import constants


def internal():
    print('=' * 5 + 'internal' + '=' * 5)
    print('constants.LED_LEFT: {}'.format(constants.LED_LEFT))
    print('constants.LED_RIGHT: {}'.format(constants.LED_RIGHT))
    print('constants.LED_LEFT_PIN: {}'.format(constants.LED_LEFT_PIN))
