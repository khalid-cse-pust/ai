def f(x):
    return -(x - 5) ** 2 + 25


def hill_climbing(start):
    current = start

    while True:
        left = current - 1
        right = current + 1

        best = current

        if f(left) > f(best):
            best = left

        if f(right) > f(best):
            best = right

        print("Current:", current, "Value:", f(current))

        if best == current:
            return current, f(current)

        current = best


print(hill_climbing(1))