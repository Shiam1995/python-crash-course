plan = ["Crash course", "Automate the boring", "C Programming",
        "Ai Modern","Yu-Gi-Oh", 'Pokemon']

print(len(plan))
plan.append("Mario")

print(plan)
plan.sort()
print(plan)
plan.sort(reverse=True)
print(plan)
del plan[-1]
print(plan)
plan.sort()
plan.insert(1,"Alexnext")
print(plan)
popped = plan.pop()
print(popped)
