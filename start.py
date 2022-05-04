"""
the main init throws you into the character selection window.
"""

import sys

from conf.conf_manager import ConfManager
from modules.__init__ import choose_capture_window


def main():
    """
    defines the runtime platform
    """

    conf = ConfManager.get('conf.json')

    if len(sys.argv) == 2 and sys.argv[1] == 'linux':
        conf['platform'] = 'linux'
    else:
        conf['platform'] = 'windows'

    ConfManager.set(conf, 'conf.json')

    choose_capture_window()


if __name__ == '__main__':
    print("Start in 1 Seconds...")

    main()
