def sum_values(a, b):
    print(a + b)
sum_values(10, 20) # Using positional arguments (order matters)
sum_values(b = 20, a = 10) # Using keyword arguments (order doesn't matter)

def sum_values(a, b=5):
    print(a + b)
sum_values(10)  # Uses default value for b

def sum_values(*args):
    print(sum(args))
sum_values(1, 2, 3, 4)  # Sums all arguments

def sum_values(**kwargs):
    print(sum(kwargs.values()))
sum_values(a=10, b=20) # Sums values of keyword arguments

def sum_values(a, b, *args, **kwargs):
    total = a + b + sum(args) + sum(kwargs.values())
    print(total)
sum_values(10, 20, 30, 40, x=50, y=60) # Sums all arguments and keyword argument values


# Lambda function 

is_even_sum = lambda x, y: True if (x + y) % 2 == 0 else False # Lambda function with ternary operator
print(is_even_sum(10, 20)) # Output: True
print(is_even_sum(10, 21)) # Output: False