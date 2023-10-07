from pp_paths.Tree import Tree


if __name__ == '__main__':
    paths = open('ip').read().split('\n')
    paths = [ p for p in paths if p.strip() != '' ]
    paths.sort()
    for i in range(len(paths)):
        if paths[i][-1] == '/':
            paths[i] = paths[i][:-1]
        dirs=paths[i].split('/')
        paths[i] = dirs
    T = Tree('///', paths, recursive=False, collapsePaths=True, commonBase=False)
    for t in T:
        print(t)
