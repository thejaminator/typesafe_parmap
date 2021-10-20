# typesafe_parmap


[![pypi](https://img.shields.io/pypi/v/typesafe-parmap.svg)](https://pypi.org/project/typesafe-parmap)
[![python](https://img.shields.io/pypi/pyversions/typesafe-parmap.svg)](https://pypi.org/project/typesafe-parmap)
[![Build Status](https://github.com/thejaminator/typesafe_parmap/actions/workflows/dev.yml/badge.svg)](https://github.com/thejaminator/typesafe_parmap/actions/workflows/dev.yml)

```
pip install pip install typesafe-parmap
```

Run functions in parallel safely with typesafe parmap!


* GitHub: <https://github.com/thejaminator/typesafe_parmap>


## Features

Easy run different functions in parallel!
```
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
assert int_result == 123, str_result == "hello world"  # should finish in 5 seconds
```

Function return types are inferred correctly by mypy / pycharm!

```
reveal_type(int_result) # mypy infers int
reveal_type(str_result) # mypy infers str
```

Got more than two functions to run? We got you covered..
```
from typesafe_parmap import par_map_3
```
... all the way to par_map_22!
