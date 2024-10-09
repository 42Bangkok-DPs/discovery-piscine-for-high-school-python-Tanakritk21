def add_one(num):
  return num + 1

my_var = 5
print("Global my_var before:", my_var)


my_var = add_one(my_var)
print("Global my_var after:", my_var)
