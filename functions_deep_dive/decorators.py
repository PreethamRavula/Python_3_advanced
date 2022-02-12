# Functions as Objects:
def add_five(num):
    print(num + 5)

print(add_five)

# Functions within Functions:
def add_five(num):
    def add_two(num):
        return num+2
    num_plus_two = add_two(10)
    print(num_plus_two + 3)
add_five(10)

# Reurning Function from a function:
def get_math_function(operation):
    def add(n1, n2):
        return n1 + n2

    def sub(n1, n2):
        return n1 - n2

    if operation == '+':
        return add

    elif operation == '-':
        return sub

add_function = get_math_function('+')
print(add_function(3, 4))

# Decorating a Function:
def title_decorator(print_name_function):
    def wrapper(*args, **kwargs):
        print("Professor: ")
        print_name_function(*args, **kwargs)
    return wrapper

def print_my_name():
    print("Preetham")

def print_joes_name():
    print("Joe")

@title_decorator
def print_name_with_lastname(name, last_name):
    print(name, last_name)

decorated_function = title_decorator(print_my_name)
decorated_function()


# Decorators:
print_joes_name()

# Decorators with parameters:
print_name_with_lastname("Preetham", "Ravula")
