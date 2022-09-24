def fibonacci(n: int) -> int:
    return fibonacci(n -1) + fibonacci(n -2)

if __name__ == "__main__":
    print(fibonacci(5))