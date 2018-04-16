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
            if ln.strip() == '':
                continue
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
    parser.add_argument('-b', '--common_base', action='store_true', help='print trees with a common base')
    parser.add_argument('-c', '--collapse_paths', action='store_true', help='collapse directory paths')
    args=parser.parse_args()
    paths = getIp()
    trees=Tree('///', paths, recursive=False, collapsePaths=args.collapse_paths, commonBase=args.common_base)
    for tree in trees:
        prettyPrintTree(tree)
        if not args.common_base and tree != trees[-1]:
            print('-*-*-')


if __name__ == '__main__':
    main()



