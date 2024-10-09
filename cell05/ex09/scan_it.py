import re
import sys

len(sys.argv)


if len(sys.argv) -1 < 2:
    print("none")
else:
    keyword = sys.argv[1]
    string = sys.argv[2]
    matches = re.findall(r"\b" + keyword + r"\b", string)
    N_matches = len(matches) + 1
    print(N_matches)
