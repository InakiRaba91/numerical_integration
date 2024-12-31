# Define the function
def func(x):
    return 2 + 0.5 * x * (x - 1) * (x - 2)

# Define the transformed function
def transformed_func(x_prime):
    a, b = 0.5, 3
    x = (x_prime + 1) * (b - a) / 2 + a
    return func(x)