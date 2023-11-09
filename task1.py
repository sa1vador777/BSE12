#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from timeit import Timer
from functools import lru_cache

def fibonacci(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)

@lru_cache
def fibonacci_lru(n: int) -> int:
    if n == 0 or n == 1:
        return n
    return fibonacci_lru(n - 2) + fibonacci_lru(n - 1)

def main(number: int = 1) -> None:

    timer_without_lru: Timer = Timer(lambda: fibonacci(40))
    time_without_lru: float = timer_without_lru.timeit(number)

    timer_with_lru: Timer = Timer(lambda: fibonacci_lru(40))
    time_with_lru: float = timer_with_lru.timeit(number)

    print(f"Время выполнения кода без инструмента: {time_without_lru}")
    print(f"Время выполнения кода с инструментом lru_cache: {time_with_lru}")

if __name__ == "__main__":
    main()
