from utils import *

class Node(object):
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = Set(lambda a,b: a.data == b.data)

    def __str__(self):
        def strip_empty(l):
            s=0
            e=len(l)-1
            while len(l[s]) == 0:
                s+=1
            while len(l[e]) == 0:
                e-=1
            return l[s:e+1]
        if len(self.children) == 0:
            return self.data
        ret=self.data+CHARS.NEW_LINE
        for c in self.children:
            ch_repr = strip_empty(c.__str__().split(CHARS.NEW_LINE))
           # ret += CHARS.PIPE_VERT+CHARS.NEW_LINE
            ret += CHARS.T_END if c == self.children[-1] else CHARS.T_MID
            ret += CHARS.PIPE_HORIZ\
                    +ch_repr[0]+CHARS.NEW_LINE
            for l in ch_repr[1:]:
                ret += (' ' if c == self.children[-1] else CHARS.PIPE_VERT)+' '
                ret += l+CHARS.NEW_LINE
        return ret


def getDirectChildren(l):
    directChildren=dict()
    for c in l:
        if len(c) == 0:
            continue
        if c[0] not in directChildren:
            directChildren[c[0]] = list()
        directChildren[c[0]].append(c)
    return directChildren


def Tree(name, lst, commonBase=True):
    tpl = getCommonPrefix(lst)
    if tpl:
        name = tpl[0]
        lst = tpl[1]
        commonBase = True
    children = list()
    directChildren = getDirectChildren(lst)
    for c in directChildren:
        n = Tree(c, [e[1:] for e in directChildren[c]], commonBase=True)[0]
        children.append(n)
    if commonBase:
        ret = Node(name)
        for n in children:
            n.parent = ret
            ret.children.add(n)
        return [ret]
    return children
