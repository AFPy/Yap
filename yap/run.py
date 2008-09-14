import sys
import os
from atomisator.main.run import atomisator

CONFIG = os.path.join(os.path.dirname(__file__), 'atomisator.cfg')

def run():
    old = sys.argv
    try:
        sys.argv = ['atomisator', '-f', CONFIG]
        atomisator()
    finally:
        sys.argv = old

