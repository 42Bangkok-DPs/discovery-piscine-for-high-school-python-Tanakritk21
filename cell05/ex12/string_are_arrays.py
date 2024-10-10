#!/usr/bin/env python3

import sys


if len(sys.argv) != 2:
    print("none")
else:
    input_string = sys.argv[1]
    if "z" not in input_string:
      print("none")
    else:
      for char in input_string:
        if char.lower() == "z": 
          print("z", end="")  
      print() 
