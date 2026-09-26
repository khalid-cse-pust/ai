
#Genetic
import random

#random.seed(0)

def fit(x):
    return x**2

pop = [random.randint(0, 31) for i in range(6)]

for i in range(10):
    pop.sort(key=fit, reverse=True)
    p1, p2 = pop[0], pop[1]
    child = (p1 + p2) // 2
    if random.random() < 0.3:
        child ^= 1
    pop[-1] = child

best = max(pop, key=fit)
print("Best:", best, "Fitness:", fit(best))
