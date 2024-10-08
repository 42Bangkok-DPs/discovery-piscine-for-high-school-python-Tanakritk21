number = int(input("Enter a number \n"))

for i in range(1,11):
  print(f"{i-1}", "x", number, f"= {(i-1)*number}")
  i -= 1
