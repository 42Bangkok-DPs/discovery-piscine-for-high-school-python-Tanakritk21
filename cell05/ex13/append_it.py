#!/usr/bin/env python3
import sys

if len(sys.argv) == 1:
    print("none")
else:
    for arg in sys.argv[1:]:
      if not arg.endswith("ism"):  # Check if it already ends with "ism"
        new_arg = arg + "ism"
        print(new_arg)
