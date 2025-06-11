def debug(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)

        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} : {v}" for k, v in kwargs.items())

        print(f"{func.__name__} with args {args_value} and kwargs {kwargs_value}")

        return result

    return wrapper


@debug
def values(name, rank="employee"):
    return f"\n{name} {rank}"


print(values("Ali", rank="Manager"))