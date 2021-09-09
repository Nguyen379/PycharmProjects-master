import random
import matplotlib.pyplot as plt


def function(x):
    return x ** 2


def derivative_function(x):
    return 2 * x


x = random.randint(-1e-2, 1e+2)
print(f"x = {x}, fx= = {derivative_function(x)}")
print()

list_lr = [2e-4, 1e-2, 1e-1, 4e-1, 1]
for lr in list_lr:
    w = x
    w_lst = [w]
    dw_lst = [function(w)]
    print(f"Learning rate is: {lr}")
    for epoch in range(1, 101):
        w = w - lr * derivative_function(w)
        dw = derivative_function(w)
        w_lst.append(w)
        dw_lst.append(function(w))
        print(f"x = {round(w, 2)}, f'x={round(dw, 2)} sau {epoch} epoch")
    print()
    plt.plot(w_lst, dw_lst, label=lr)
    print("plot")

plt.xlabel('x')
plt.ylabel("f'(x)")
plt.title('Loss Function')

plt.tight_layout()
plt.legend()
plt.show()
