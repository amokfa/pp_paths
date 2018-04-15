# `pp_paths`: A python script to pretty print directory structures

pass the paths of files to be printed through `stdin`. They will be printed as a tree using ascii art.

    > find b -type f|pp_paths
    b/
    ├─a/b/c/d/
    │ ├─1
    │ ├─2
    │ └─3
    │
    ├─s
    ├─b
    │ ├─q
    │ └─x
    │
    ├─r
    └─q
      ├─e
      └─y

## TODO:

. An ncurses interface similar to vim folds?

. add some formatting options

. for some reason, modules don't work properly if loaded from the repl 

. Integrate it with ranger