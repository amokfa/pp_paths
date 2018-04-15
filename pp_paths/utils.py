def toPath(lst):
    ret = ''
    for p in lst:
        ret += p+'/'
    return ret

def getCommonPrefix(paths):
    common=list()
    fst=paths[0]
    for i in range(len(fst)):
        for p in paths[1:]:
            if fst[i] == p[i] and i == len(fst)-1:
                return toPath(fst[:i+1]), [ p[i+1:] for p in paths ]
            if fst[i] != p[i]:
                return toPath(fst[:i]), [ p[i:] for p in paths ]
    return None

class CHARS():
    PIPE_VERT='│'
    T_MID='├'
    PIPE_HORIZ='─'
    NEW_LINE='\n'
    T_END='└'

class Set(object):
    def __init__(self, f):
        self.equal = f
        self._elems = list()

    def add(self, o):
        for e in self._elems:
            if self.equal(o,e):
                return
        self._elems.append(o)

    def __len__(self):
        return len(self._elems)

    def __iter__(self):
        for e in self._elems:
            yield e

    def __getitem__(self, n):
        return self._elems[n]

