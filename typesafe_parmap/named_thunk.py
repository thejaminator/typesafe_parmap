from typing import Generic, TypeVar, Callable

T = TypeVar("T")
# Util class so that the logger for par_map_timeout_n knows what function it is logging for
class NamedThunk(Generic[T]):
    def __init__(self, thunk: Callable[[], T], name: str):
        self.thunk = thunk
        self.name = name

    def __call__(self) -> T:
        return self.thunk()

    @property
    def __name__(self) -> str:
        return self.name
