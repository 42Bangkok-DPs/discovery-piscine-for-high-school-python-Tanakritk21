import sys

def shrink(string):
    return string[:8]

def enlarge(string):
    return string + 'Z' * (8 - len(string))

if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            if len(arg) > 8:
                print(shrink(arg))
            elif len(arg) < 8:
                print(enlarge(arg))
            else:
                print(arg)
else:
        print("none")
