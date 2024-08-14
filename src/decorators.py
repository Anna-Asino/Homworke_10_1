from functools import wraps
from typing import Any, Callable


def log(filename: Any = None) -> Callable:
    """Декоратор, который логирует вызов функции и ее результат в файл и консоль"""

    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            try:
                result = func(*args, **kwargs)
                log_messege = f'my_function ok \n'
                # with open(filename, "a", encoding="utf-8") as file:

            except Exception as e:
                result = None
                log_messege = f'my_function error: {e}. Inputs: {args}, {kwargs} \n'
            if filename:
                with open(filename, "a", encoding="utf-8") as file:
                    file.write(log_messege)
            else:
                print(log_messege)
            return result
        return wrapper
    return decorator


@log(filename="mylog.txt")
def my_function(x, y):
    return x + y


if __name__ == "__main__":
    print(my_function('2', 2))