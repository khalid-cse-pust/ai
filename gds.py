import numpy as np
def f(x):
    return x**2-4*x+4
def df(x):
    return 2*x-4

def gds(s,lr=0.1,it=50,t=1e-6):
    x=s
    for i in range(it):
        grad=df(x)
        x_new=x-lr*grad

        if abs(x_new-x)<t:
            break
        x=x_new
        print(f"Iteration{i+1}:x={x:.6f},f(x)={f(x):.6f}")
    return x, f(x)
s_point=0
lr=0.1
x_min,f_min=gds(s_point,lr)

print("\nMinimum value found at x=" , x_min)
print("f(x)",f_min)