#`pp_paths`: A python script to pretty print directory structures

pass the paths of files to be printed through `stdin`. They will be printed as a tree using ascii art.

    > find b|python main.py
    base
    └─b
      ├─a
      ├─s
      ├─b
      │ ├─q
      │ └─x
      ├─r
      └─q
        ├─e
        └─y
        
        
##TODO:

1. An ncurses interface similar to vim folds?
2. make a package
3. usablity with relative paths
4. common base should be optional
5. merge common path prefix
6. fix printing bugs