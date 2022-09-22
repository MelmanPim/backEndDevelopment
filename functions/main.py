# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

def greet(name):
    greeting = f"Hello, {name}!"
    return greeting

print(greet('Bob'))


def add(a, b, c):
    sum = a + b + c
    return sum

print(add(5,3,2))

def positive(x):
    return x > 0

print(positive(50))
print(positive(-50))
print(positive(0))

def negative(x):
    return x < 0

print(negative(50))
print(negative(-50))
print(negative(0))

