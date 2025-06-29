import functools


def log(filename=None):
    """
    Декоратор для логирования начала и конца выполнения функции,
    а также ошибок, возникших при выполнении.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # определяем функцию для записи логов
            def write_log(message):
                if filename:
                    with open(filename, "a", encoding="utf-8") as f:
                        f.write(message + '\n')
                else:
                    print(message)

            # логируем начало выполнения функции
            try:
                result = func(*args, **kwargs)
                # логируем успешное завершение и результат
                write_log(f"{func.__name__} ok")
                return result
            except Exception as e:
                # логируем ошибку с типом и входными параметрами
                error_type = type(e).__name__
                write_log(f"{func.__name__} error: {error_type}. Inputs: {args}, {kwargs}")
                # перебрасываем исключение дальше
                raise
        return wrapper
    return decorator
