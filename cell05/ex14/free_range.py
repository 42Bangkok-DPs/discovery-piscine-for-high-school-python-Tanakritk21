#!/usr/bin/env python3

import sys

num_args = len(sys.argv) - 1


if num_args != 2:
    print("none")

start_num = int(sys.argv[1])
end_num = int(sys.argv[2])

number_array = list(range(start_num, end_num + 1))

print(number_array)
