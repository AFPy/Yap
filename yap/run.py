import sys
from os.path import dirname, join
from atomisator.main.run import atomisator

CONFIG = join(dirname(dirname(__file__)), 'atomisator.cfg')

def run():
    old = sys.argv
    try:
        sys.argv = ['atomisator', '-f', CONFIG]
        atomisator()
    finally:
        sys.argv = old

