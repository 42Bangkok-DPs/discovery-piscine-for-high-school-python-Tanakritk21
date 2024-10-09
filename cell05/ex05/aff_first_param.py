import sys

num_of_params = len(sys.argv) - 1

if num_of_params > 0 :
    print(sys.argv[1])
elif num_of_params == 0:
    print("none")
