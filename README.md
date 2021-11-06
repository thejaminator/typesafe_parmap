# Typesafe parmap


[![pypi](https://img.shields.io/pypi/v/typesafe-parmap.svg)](https://pypi.org/project/typesafe-parmap)
[![python](https://img.shields.io/pypi/pyversions/typesafe-parmap.svg)](https://pypi.org/project/typesafe-parmap)
[![Build Status](https://github.com/thejaminator/typesafe_parmap/actions/workflows/dev.yml/badge.svg)](https://github.com/thejaminator/typesafe_parmap/actions/workflows/dev.yml)

```
pip install typesafe-parmap
```

Run functions in parallel safely with your type checkers


* GitHub: <https://github.com/thejaminator/typesafe_parmap>


## Features

Easy run different functions in parallel
```python
from typesafe_parmap import par_map_2
import time
from concurrent.futures import ThreadPoolExecutor

tp = ThreadPoolExecutor(5)

def long_running_int(param: int) -> int:
    time.sleep(5)  # long IO task here
    return 123

def long_running_str(param: str) -> str:
    time.sleep(5)  # long IO task here
    return "hello world"

int_result, str_result = par_map_2(
                        lambda: long_running_int(5),
                        lambda: long_running_str("test"),
                        executor=tp)
assert int_result == 123, str_result == "hello world"  # should finish in around 5 seconds
```

Function return types are inferred correctly by mypy / pycharm

```python
reveal_type(int_result) # mypy infers int
reveal_type(str_result) # mypy infers str
```

Accidentally unpacked too many / little values? Type inference checks that for you!
```python
one, two, three, four = par_map_3(
        lambda: long_running_int(5), lambda: long_running_str("test"), lambda: "something", executor=tp
    ) # Error: Need more than 3 values to unapck, (4 expected)
```

Got more than a few functions to run? We got you covered...
```python
from typesafe_parmap import par_map_4 # ... all the way to par_map_22!
```

Want to change the number of functions to run in parallel? Hate having to import a different one each time?
Use par_map_n!
```python
from typesafe_parmap import par_map_2, par_map_3, par_map_n
a = par_map_2(lambda: long_running_int(5), lambda: long_running_str("test"), executor=executor)
b = par_map_n(lambda: long_running_int(5), lambda: long_running_str("test"), executor=executor)

assert a == b

c = par_map_3(
    lambda: long_running_int(5),
    lambda: long_running_str("test"),
    lambda: long_running_str("test"),
    executor=executor,
)
d = par_map_n(
    lambda: long_running_int(5),
    lambda: long_running_str("test"),
    lambda: long_running_str("test"),
    executor=executor,
)

assert c == d
```


