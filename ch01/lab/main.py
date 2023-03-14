import random

#Part A
weeks = 16
classes = 5
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
print("Cost per week:", cost_per_week)
classes_per_week = 3
cost_per_class = cost_per_week/classes_per_week
print("The cost per class is ", cost_per_class)
print(classes_per_week, type(classes_per_week))
print(cost_per_class, type(cost_per_class))

#Part B
obj_list = [12, "gummies", "soymilk", 10.28, "donut", "banana"]
obj = random.choice(obj_list)
print("A random object: ", obj)
