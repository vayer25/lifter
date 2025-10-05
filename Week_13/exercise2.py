def numbers_only(func):
    def wrapper(*args, **kwargs):
        for arg in list(args) + list(kwargs.values()):
            if not isinstance(arg, (int, float)):
                raise TypeError(f"All arguments must be numbers, but got {type(arg).__name__}")
        return func(*args, **kwargs)
    return wrapper


@numbers_only
def add(a, b):
    return a + b



print(add(5, 3))     
print(add("hola", 6))   
