import time


def time_decorator(func):
    def wrapp(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = (end_time - start_time) * 1000  # переводим секунды в миллисекунды
        print(f"Время выполнения функции {func.__name__}: {execution_time:.2f} миллисекунд")
        return result
    return wrapp
