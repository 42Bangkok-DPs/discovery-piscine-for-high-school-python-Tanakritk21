first_number = int(input("Enter your first number : \n"))
second_number = int(input("Enter your second number : \n"))

 print(first_number, " x ", second_number, " = " ,first_number*second_number)

if first_number*second_number < 0:
  print("This number is negative.")
elif first_number*second_number  > 0:
  print("This number is positive.")
else:
  print("This number is both positive and negative.")
