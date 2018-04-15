import curses as cs
import os
import sys
import argparse
from .utils import *
from .Tree import *


def getIp():
    paths = list()
    try:
        while True:
            ln=input()
            dirs=ln.split('/')
            paths.append(dirs)
    except Exception as e:
        pass
    return paths

def runUi(tree):
    pass

def prettyPrintTree(tree):
    print(tree.__str__())


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-b', '--base', action='store_true', help='print with a common base')
    # parser.add_argument('-d', '--dump', action='store_true', help='dump common prefix')
    args=parser.parse_args()
    paths = getIp()
    trees=Tree('base', paths, args.base)
    for tree in trees:
        prettyPrintTree(tree)


if __name__ == '__main__':
    main()



