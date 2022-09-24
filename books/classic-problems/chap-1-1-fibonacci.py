from typing import Dict

memoized: Dict[int, int] = {0:0, 1:1}

def fibonacci(n: int) -> int:
    if n not in memoized:
        memoized[n] = fibonacci(n -1) + fibonacci(n -2)
    return memoized[n]

if __name__ == "__main__":
    print(fibonacci(150))