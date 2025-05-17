import math

def solve_quadratic(a, b, c):
    if a == 0:
        raise ValueError("Coefficient 'a' cannot be zero.")

    discriminant = b ** 2 - 4 * a * c

    if discriminant < 0:
        return (0, None, None)  # No real roots
    elif discriminant == 0:
        root = -b / (2 * a)
        return (1, root, root)  # One real root
    else:
        sqrt_d = math.sqrt(discriminant)
        root1 = (-b + sqrt_d) / (2 * a)
        root2 = (-b - sqrt_d) / (2 * a)
        return (2, root1, root2)  # Two real roots
