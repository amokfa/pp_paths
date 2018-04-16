# `pp_paths`: A python script to pretty print directory structures

pass the paths of files to be printed through `stdin`. They will be printed as a tree using ascii art.


> pp_paths [-c] [-b]

*-c* collapse directory sequences

*-b* print trees with a common base named '////'. The default is to print all the
    trees formed separated with a '*////*'

## Examples

    > find b -type f|pp_paths
    b/
    ├─a/
    │ └─b/
    │   └─c/
    │     └─d/
    │       ├─1
    │       ├─2
    │       └─3
    │
    │
    │
    │
    ├─s
    ├─b/
    │ ├─w/
    │ │ └─a
    │ │
    │ ├─q
    │ └─x
    │
    ├─r
    └─q/
      ├─e
      └─y


    > find b -type f|pp_paths -c
    b/
    ├─a/b/c/d/
    │ ├─1
    │ ├─2
    │ └─3
    │
    ├─s
    ├─b/
    │ ├─w/a
    │ ├─q
    │ └─x
    │
    ├─r
    └─q/
      ├─e
      └─y

    > {find b -type d; find a}|pp_paths
    b/
    ├─a/
    │ └─b/
    │   └─c/
    │     └─d
    │
    │
    │
    ├─b/
    │ └─w
    │
    ├─z
    └─q
    
    -*-*-
    a/
    └─b
    
    user@machine /dev/pts/4 /home/user/src/pp_paths
    > {find b -type d; find a}|pp_paths -b
    ////
    ├─b/
    │ ├─a/
    │ │ └─b/
    │ │   └─c/
    │ │     └─d
    │ │
    │ │
    │ │
    │ ├─b/
    │ │ └─w
    │ │
    │ ├─z
    │ └─q
    │
    └─a/
      └─b

## TODO:

. An ncurses interface similar to vim folds?

. add some formatting options

. for some reason, modules don't work properly if loaded from the repl 

. Integrate it with ranger

. Find a better name for common base name(pass a name at cli)

. -c doesn't collapse directories if they were an external node in ip.