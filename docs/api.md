# How to run

E.g
```
import time
from concurrent.futures import ThreadPoolExecutor

tp = ThreadPoolExecutor(5)

def long_running_int(param: int) -> int:
    time.sleep(5)  # long IO task here
    return 123

def long_running_str(param: str) -> str:
    time.sleep(5)  # long IO task here
    return "hello world"

int_result, str_result = par_map_2(lambda: long_running_int(5), lambda: long_running_str("test"), executor=tp)
assert int_result == 123, str_result == "hello world"  # should finish in 5 seconds

```
