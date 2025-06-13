from datetime import datetime


def log_function_call(func):
    def wrapper(*args, **kwargs):
        args_value = ", ".join(str(arg) for arg in args)
        kwargs_value = ", ".join(f"{k} : {v}" for k, v in kwargs.items())

        dt = datetime.now().strftime("Date: %Y:%m:%d  Time: %I:%M:%S")

        print(
            f"{func.__name__} function is called at {dt}; \nWith args: {args_value} and kwargs: {kwargs_value}"
        )

        result = func(*args, **kwargs)

        return result

    return wrapper


@log_function_call
def random(name, rank, age):
    return ""


# In python args should appear before kwargs:

print(random("Hassan", "Student", age=18))