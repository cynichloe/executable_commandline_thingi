# executable_commandline_thingi


## to install the executable, run under root 
```
python3 setup.py develop
```

this will create an executable called `Fangi` in dev mode, which can be executed by calling 
```fangi [commands]
```

## The 2 commands available at the moment are described in the `click_group.py`: 
1. `hello`
2. `goodbye`

## So, the following 2 commands are supported:
1. `fangi hello`
2. `fangi goodbye`

## In the end, should one be not happy with the executable, one can easily uninstall the executable by
```
python3 setup.py develop --uninstall
```
