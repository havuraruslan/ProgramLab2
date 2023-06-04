import math
def num(a, b, c):
    E = (a + 4*b + c) / 6
    SD = (c - a) / 6
    return E, SD

tasks = []

a = float(input("Enter the number 1: "))
b = float(input("Enter the number 2: "))
c = float(input("Enter the number 3: "))
tasks.append((a, b, c))

E_tasks, SD_tasks = zip(*[num(*task) for task in tasks])

E_project = sum(E_tasks)
SD_project = math.sqrt(sum(sd**2 for sd in SD_tasks))

CI_min = E_project - 2*SD_project
CI_max = E_project + 2*SD_project

print(f"Project's 95% confidence interval: {CI_min:.2f} ... {CI_max:.2f} points")