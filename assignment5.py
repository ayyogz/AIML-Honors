def output_decorator(parameter):
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(parameter)
            print(args)
            print(result)
           
            return result
        return wrapper
    return decorator
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        result = func(*args, **kwargs)
        print(result)
        return result
    return wrapper

@output_decorator("addition")
def add(a, b):
    return a + b
@output_decorator("string concat")
def concat_strings(a, b):
    return a + b
@output_decorator("multiplication")
def multiply(a, b):
    return a * b
@log_execution
def complex_calc(x, y, z):
    return (x + y) * z - x
@output_decorator("division")
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError()
    return a / b
print('addition test')
add(10, 20)

print('string test')
concat_strings('hello ', 'world')
print('multiplication test')
multiply(5, 6)

print('complex calc test')
complex_calc(3, 4, 2)
print('division test')
divide(15, 3)

print('division by zero')
try:
    divide(10, 0)
except ZeroDivisionError:
    print('caught it')
print('final test')
add(100, 200)
